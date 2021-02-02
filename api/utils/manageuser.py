from api.models.postgres.profile import Profile
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class ManageUser:

    def __init__(self, username, password, email=None):
        self.username = username
        self.email = email
        self.password = password

    def add(self, job_type):
        user = User.objects.create_user(username=self.username,
                                        password=self.password,
                                        email=self.email)
        user.save()
        agent, is_updated = Agent.objects.update_or_create(
            user=user,
            job_type=job_type,
            status=1
        )

        return agent.user_id

    def update_password(self, new_password):
        user = User.objects.get(username=self.username)
        user.set_password(new_password)
        user.save()
        return True

    def authenticate(self):
        user = authenticate(username=self.username, password=self.password)
        return user
