from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('edit/', views.editor_view, name='editor_view'),
    path('about/', views.about_editor_view, name='about_editor'),
    path('search/', views.search_view, name='search_view')
]
