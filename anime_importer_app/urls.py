from django.urls import path

from .views import index, AddFile, success_file

urlpatterns = [
    path('', index, name='index'),
    path('addfile/', AddFile.as_view(), name='addfile'),
    path('success_file/', success_file, name='success_file'),
]
