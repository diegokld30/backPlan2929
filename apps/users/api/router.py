from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.users.api.views import RegisterView, UserView , UserListView


urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/me', UserView.as_view()),
    path('auth/users/', UserListView.as_view()),  # Ruta para listar usuarios

]