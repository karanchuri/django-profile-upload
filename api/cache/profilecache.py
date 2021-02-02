from api.adapters.redis.rediscacheadapter import RedisCacheAdapter
from api.adapters.redis.basecachehandler import BaseCacheHandler
from api.serializer.profileserializer import ProfileSerializer
from api.models.postgres.profile import Profile


class ProfileCache(BaseCacheHandler):
    BASE_KEY = "profile_cache__USER_ID__"

    def __init__(self, user_id):
        self.user_id = user_id
        self.value = None
        key = self.BASE_KEY.replace("__USER_ID__", str(user_id))
        super().__init__(key=key, timeout=60 * 60 * 24)

    def get_configuration(self):
        _cached_content = RedisCacheAdapter.get(
            self.key, machine_alias=self.machine_alias
        )
        if _cached_content:
            self.value = _cached_content
            return self.value
        else:
            profile = Profile.objects.filter(user_id=self.user_id).first()
            serialized_picture = ProfileSerializer(profile)
            data = serialized_picture.data
            self.value = data
            self.set_configuration(data)
            return data
