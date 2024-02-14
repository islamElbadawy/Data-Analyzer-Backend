from django.urls import path
from .views import DataCreateView

urlpatterns = [
    path('data/', DataCreateView.as_view(), name='data-create'),
]