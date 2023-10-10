from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# 회원가입기능
from users import views



urlpatterns = [
    path('signup/', views.Signup.as_view(),name="signup"),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),   # 토큰 방식의 로그인 urls 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('follow/<int:user_id>/', views.Follow_View.as_view(), name="follow"),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    
]

