from api.models.postgres.profilepicture import ProfilePictures
from rest_framework import serializers


class ProfilePictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfilePictures
        fields = (
            "url",
            "is_primary",
            "image_index"
        )
