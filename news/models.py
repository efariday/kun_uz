from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from users.models import User


class Category(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Tag(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class News(BaseModel):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to="news/images", null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="news"
    )
    category = models.ForeignKey(
        "news.Category", on_delete=models.SET_NULL, null=True, blank=True, related_name="news"
    )
    tags = models.ManyToManyField("news.Tag", blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")


class Comment(BaseModel):
    news = models.ForeignKey(
        "news.News", on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="news_comments"
    )
    text = models.TextField(max_length=500, null=False, blank=False)
    parent = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="children"
    )
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment({self.id})"

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


class MediaFile(BaseModel):
    news = models.ForeignKey(
        "news.News", on_delete=models.CASCADE, related_name="media_files"
    )
    file = models.FileField(upload_to="news/media/")

    def __str__(self):
        return f"{self.news.title} - MediaFile({self.id})"

    class Meta:
        verbose_name = _("Media File")
        verbose_name_plural = _("Media Files")
