from api.models.postgres.profile import Profile


class UpdateProfileController:

    def __init__(self, data, user_id):
        self.data = data
        self.user_id = user_id
        self._parse_data()

    def _parse_data(self):
        self.params = {}

        if self.data.get("name"):
            self.params["name"] = self.data.get("name")

        if self.data.get("age"):
            self.params["age"] = int(self.data.get("age"))

        if self.data.get("skills"):
            self.params["skills"] = self.data.get("skills")

    def save_profile(self):
        profile = Profile.objects.filter(user_id=self.user_id).first()
        if profile:
            Profile.objects.update(**self.params)
        else:
            self.params["user_id"] = self.user_id
            Profile.objects.create(**self.params)
