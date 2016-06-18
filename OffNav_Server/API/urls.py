from django.conf.urls import patterns, include, url
from rest_framework.authtoken import views as view_auth
import views

urlpatterns = [
    url(r'^directions/', views.directions),
]