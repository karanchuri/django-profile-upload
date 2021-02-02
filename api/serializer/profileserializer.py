from api.serializer.profilepictureserializer import ProfilePictureSerializer
from api.models.postgres.profile import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    profile_pictures = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            "name",
            "age",
            "skills",
            "profile_pictures"
        )

    def get_skills(self, profile):
        return profile.skills

    def get_profile_pictures(self, profile):
        if not hasattr(profile, "profile_pictures"):
            return None
        pictures = profile.profile_pictures.all()
        if len(pictures) == 0:
            return None
        serialized_picture = ProfilePictureSerializer(pictures, many=True)
        return serialized_picture.data
