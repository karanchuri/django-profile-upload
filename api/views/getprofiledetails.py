from api.decorators.authentication import cinta_authentication
from django.utils.decorators import method_decorator
from api.cache.profilecache import ProfileCache
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class GetProfile(APIView):

    @method_decorator(cinta_authentication())
    def get(self, request):
        cache = ProfileCache(user_id=request.cinta_user_id)
        cache.get_configuration()
        return Response(status=status.HTTP_200_OK, data=cache.value)
