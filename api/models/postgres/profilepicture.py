from api.models.postgres.profile import Profile
from django.db import models


class ProfilePictures(models.Model):
    profile = models.ForeignKey(Profile, related_name="profile_pictures", on_delete=models.PROTECT)
    url = models.CharField(max_length=500, null=True, db_index=True)
    is_primary = models.BooleanField(db_index=True, default=False)
    image_index = models.IntegerField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        app_label = 'api'
        unique_together = ('profile', 'image_index')
