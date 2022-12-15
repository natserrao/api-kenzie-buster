from django.urls import path
from .views import RegisterView, LoginView, UserDetailView

urlpatterns = [
    path("users/", RegisterView.as_view()),
    path("users/login/", LoginView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
]
