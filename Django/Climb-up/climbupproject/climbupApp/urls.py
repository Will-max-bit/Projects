from django.urls import path
from . import views

app_name='climbupApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('load_posts/', views.load_posts, name='load_posts'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('profile_load/', views.profile_load, name='profile_load'),
    path('login_page/', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('post_new/', views.post_new, name='post_new'),
    path('get_cities/', views.get_cities, name='get_cities'),
    path('add_city/', views.add_city, name='add_city'),
    path('like_post/', views.like_post, name='like_post'),
    path('attendants/', views.attendants, name='attendants'),
    path('post_edit/', views.post_edit, name='post_edit'),
    path('delete_post/', views.delete_post, name='delete_post'),
    path('load_comments/', views.load_comments, name='load_comments'),
    path('save_comment/', views.save_comment, name='save_comment'),
]
