from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:id>', views.post, name='post'),
    path('create', views.create, name='create'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('edit/<str:id>', views.edit, name='edit'),
    path('update/<str:id>', views.update, name='update'),
]