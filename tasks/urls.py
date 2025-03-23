from django.urls import path
from tasks.views import show_patern

urlpatterns = [
    path("show_patern/", show_patern)
]