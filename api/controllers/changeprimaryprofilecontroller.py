from api.models.postgres.profilepicture import ProfilePictures
from api.cache.profilecache import ProfileCache


class ChangePrimaryProfileController:

    def __init__(self, user_id, image_index):
        self.image_index = image_index
        self.user_id = user_id

    def mark_all_non_primary(self):
        ProfilePictures.objects.filter(profile__user_id=self.user_id).update(is_primary=False)

    def mark_requested_as_primary(self):
        ProfilePictures.objects.filter(profile__user_id=self.user_id, image_index=self.image_index).\
            update(is_primary=True)

    def clear_cache(self):
        ProfileCache(user_id=self.user_id).invalidate_cache()
