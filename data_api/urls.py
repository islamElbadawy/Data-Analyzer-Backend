from django.urls import path
from .views import process_data

urlpatterns = [
    path('data/', process_data, name='data-create'),
]