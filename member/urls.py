from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('mypage/', views.userinfo, name='mypage'),
    path('userpage/<str:writer>', views.user_select_info, name='userpage'),
    path('profile_update', views.ProfileUpdateView.as_view(), name='profile_update'),
]
