from django.urls import path

from .views import *

urlpatterns = [
    path('', ScrapperViewForm.as_view(), name='index'),
    path('results/', results, name='results'),
]
