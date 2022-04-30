from .views import shorten, get_url, stats
from django.urls import path

urlpatterns = [
    path('/shorten/<shortcode>', shorten),
    path('/get-url/<shortcode>', get_url),
    path('/stats/<shortcode>', stats),
]