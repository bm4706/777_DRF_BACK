from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# 회원가입기능
from users import views



urlpatterns = [
    path('signup/', views.Signup.as_view(),name="signup"),
]