from django.conf.urls import include, url

urlpatterns = [
    url(r'api/profile/', include('api.urls')),
]
