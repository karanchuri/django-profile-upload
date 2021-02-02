from rest_framework.response import Response

from api.models import Profile
from api.utils.manageuser import ManageUser
from rest_framework.views import APIView
from rest_framework import status


class RegisterView(APIView):

    def post(self, request):
        password = request.data.get("password")
        email = request.data.get("email")

        if password is None or email is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        manage = ManageUser(username=email, password=password, email=email)
        user_id = manage.add()

        profile = Profile.objects.filter(user_id=user_id).first()
        if not profile:
            Profile.objects.create(user_id=user_id)

        if not user_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        token = manage.authenticate()

        if token:
            return Response(data={"token": token}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
