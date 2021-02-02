from api.controllers.updateprofilecontroller import UpdateProfileController
from api.decorators.authentication import cinta_authentication
from django.utils.decorators import method_decorator
from api.cache.profilecache import ProfileCache
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class UpdateProfile(APIView):

    @method_decorator(cinta_authentication())
    def post(self, request):
        data = request.data
        update_controller = UpdateProfileController(data=data, user_id=request.cinta_user_id)
        update_controller.save_profile()
        ProfileCache(user_id=request.cinta_user_id).invalidate_cache()
        return Response(status=status.HTTP_200_OK)
