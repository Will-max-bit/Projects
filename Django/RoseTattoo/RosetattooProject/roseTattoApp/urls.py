from django.urls import path
from . import views

app_name='roseTattoApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('artists_page/', views.artists_page, name='artists_page'),
    path('artist1/', views.artist1, name='artist1'),
    path('artist2/', views.artist1, name='artist2'),
    path('artist3/', views.artist1, name='artist3'),
    path('artist4/', views.artist1, name='artist4'),
    path('contact_us/', views.contact_us, name='contact_us'),
]