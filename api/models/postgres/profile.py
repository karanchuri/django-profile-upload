from django.contrib.postgres.fields import ArrayField
from api.models.postgres.skills import Skills
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.PROTECT, related_name="profile")
    name = models.CharField(max_length=100, null=True, db_index=True)
    age = models.IntegerField(db_index=True)
    skills = models.ManyToManyField(Skills, related_name="profile", default=None)
    user_defined_skills = ArrayField(ArrayField(models.CharField(max_length=50, blank=True), size=8), size=8)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
