from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_blogpost', views.new_blogpost, name='new_blogpost'),
    path('edit_blogpost/<int:blogpost_id>/', views.edit_blogpost, name='edit_blogpost'),
]