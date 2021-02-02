from django.conf.urls import url
from api import views

urlpatterns = [
    url(r"health/+$", views.HealthView.as_view(), name="health"),
    url(r"get-profile-details/+$", views.GetProfile.as_view(), name="get_profile"),
    url(r"get-profile-image/+$", views.GetProfileImage.as_view(), name="get_profile-image"),
    url(r"change-primary-profile/+$", views.ChangePrimaryProfile.as_view(), name="change_primary_profile"),
    url(r"login/+$", views.LoginView.as_view(), name="login"),
    url(r"register/+$", views.RegisterView.as_view(), name="register"),
    url(r"update-profile/+$", views.UpdateProfile.as_view(), name="update_profile"),
    url(r"update-image/(?P<image_index>[0-9]+$)", views.UpdateProfilePicture.as_view(), name="update_profile_image"),
]
