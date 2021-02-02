from django.conf.urls import url
from api import views

urlpatterns = [
    url(r"health/+$", views.HealthView.as_view(), name="health"),
]
