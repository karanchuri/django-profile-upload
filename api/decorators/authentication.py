from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from functools import wraps
import traceback


def cinta_authentication():
    def not_authorized():
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def decorator(view_func):
        @wraps(view_func)
        def _validate(request, *args, **kwargs):
            request.cinta_user_id = None
            try:
                token_key = request.META.get("HTTP_AUTHORIZATION", None)
                token_key = token_key.replace("Bearer ", "")
            except:
                print(traceback.format_exc())
                return not_authorized()

            token = Token.objects.filter(key=token_key).first()

            if not token:
                return not_authorized()

            request.cinta_user_id = token.user_id

            return view_func(request, *args, **kwargs)

        return _validate

    return decorator
