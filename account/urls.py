from django.urls import path
from . import views

app_name='account'
urlpatterns = [
    path('register/',views.Register.as_view(),name='register'),
    path('login/',views.User_login.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('profile/<int:user_id>',views.UserProfileView.as_view(),name='user_profile'),
    path("follow/<int:user_id>/", views.UserFollowView.as_view(), name="user-follow"),
    path("unfollow/<int:user_id>/",views.UserUnFollowView.as_view(),name="user-unfollow"),
]
