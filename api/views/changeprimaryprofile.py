from api.controllers.changeprimaryprofilecontroller import ChangePrimaryProfileController
from api.decorators.authentication import cinta_authentication
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ChangePrimaryProfile(APIView):

    @method_decorator(cinta_authentication())
    def patch(self, request):
        data = request.data
        image_index = data.get("image_index")
        controller = ChangePrimaryProfileController(user_id=request.cinta_user_id, image_index=image_index)
        controller.mark_all_non_primary()
        controller.mark_requested_as_primary()
        controller.clear_cache()
        return Response(status=status.HTTP_200_OK)
