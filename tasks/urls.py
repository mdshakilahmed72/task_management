from django.urls import path
from tasks.views import show_patern,show_specific_task

urlpatterns = [
    path("show_patern/", show_patern),
    path("show_patern/<int:id>",show_specific_task)
]