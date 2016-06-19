from django.conf.urls import patterns, include, url
import views

urlpatterns = [
    url(r'^directions/', views.directions),
]