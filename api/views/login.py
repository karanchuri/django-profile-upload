from rest_framework.response import Response
from api.utils.manageuser import ManageUser
from rest_framework.views import APIView
from rest_framework import status


class LoginView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if username is None or password is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        manage = ManageUser(username=username, password=password)
        token = manage.authenticate()

        if token:
            return Response(data={"token": token}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
