from django.core import signing
from django.conf import settings
import random
import string

TOKEN_SALT = 'email-confirm-salt'
TOKEN_EXPIRATION = 60 * 60 * 24  # 1 kun (sekundda)

def generate_email_confirm_token(user):
    data = {'user_id': user.id}
    token = signing.dumps(data, salt=TOKEN_SALT)
    return token

def verify_email_confirm_token(token):
    try:
        data = signing.loads(token, salt=TOKEN_SALT, max_age=TOKEN_EXPIRATION)
        return data.get('user_id')
    except signing.BadSignature:
        return None
    except signing.SignatureExpired:
        return None

def generate_temporary_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
