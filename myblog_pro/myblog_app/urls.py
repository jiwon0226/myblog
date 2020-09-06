from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.create_board, name="create_board"),
    path('read/', views.read_board, name="read_board"),
    path('detail/<int:pk>', views.read_detail, name="read_detail"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('signup/', views.sign_up, name="sign_up"),
]
