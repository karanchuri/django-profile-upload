from api.cache.profilecache import ProfileCache
from api.controllers.imageuploadcontroller import ImageUploadController
from api.decorators.authentication import cinta_authentication
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import os


class UpdateProfilePicture(APIView):

    @method_decorator(cinta_authentication())
    def post(self, request, image_index):
        up_file = request.FILES["file"]
        f, file_extension = os.path.splitext(up_file.name)
        if file_extension.lower() not in [".jpg", ".png"]:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        controller = ImageUploadController(user_id=request.cinta_user_id, image_index=image_index, up_file=up_file)
        controller.save_image()
        controller.compress_image()

        if controller.is_duplicate():
            return Response(status=status.HTTP_208_ALREADY_REPORTED)

        controller.update_db()
        ProfileCache(user_id=request.cinta_user_id).invalidate_cache()
        return Response(status=status.HTTP_200_OK)
