from rest_framework.views import APIView
from django.views.static import serve
import os


class GetProfileImage(APIView):

    def get(self, request):
        file_path = request.query_params.get("file_name")
        return serve(request, os.path.basename(file_path), os.path.dirname(file_path))
