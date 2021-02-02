from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class ManageUser:

    def __init__(self, username, password, email=None):
        self.username = username
        self.email = email
        self.password = password

    def add(self):
        try:
            user = User.objects.create_user(username=self.username,
                                            password=self.password,
                                            email=self.email)
            return user.id
        except:
            return None

    def update_password(self, new_password):
        user = User.objects.get(username=self.username)
        user.set_password(new_password)
        user.save()
        return True

    def authenticate(self):
        user = authenticate(username=self.username, password=self.password)
        if not user:
            return None
        token, is_created = Token.objects.get_or_create(user=user)
        return token.key
