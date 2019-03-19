from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.ListPost.as_view()),
    path('api/<int:pk>/', views.DetailPost.as_view()),
]