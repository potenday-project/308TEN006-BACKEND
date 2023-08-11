from django.urls import path
from . import views

urlpatterns = [
    path('signup/<str:profile_img>/<str:nickname>', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('mypage/', views.userinfo, name='mypage'),
    path('userpage/<str:writer>', views.user_select_info, name='userpage'),
    path('profile_update', views.ProfileUpdateView.as_view(), name='profile_update'),
    ## 회원가입 로직
    path('signup_1/', views.signup_1, name='signup_1'),
    path('signup_2/<str:profile_img>/', views.signup_2, name='signup_2'),
]
