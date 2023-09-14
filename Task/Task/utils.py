import datetime
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings

def jwt_payload_handler(user):
    """
    Custom JWT payload handler for the Customer model.

    This function is responsible for creating the payload that is encoded into
    the JWT (JSON Web Token) for the Customer model.

    :param user: The Customer instance for whom the JWT is being generated.
    :type user: Customer model instance

    :return: The payload to be encoded into the JWT.
    :rtype: dict
    """
    user_model = get_user_model()
    username_field = user_model.USERNAME_FIELD

    payload = {
        'user_id': user.pk,
        'username': getattr(user, username_field),
        'exp': datetime.datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
        'iat': datetime.datetime.utcnow()
    }

    # Add custom claims or additional user information to the payload if needed
    # For example, you can include the user's email:
    # payload['email'] = user.email

    return payload
