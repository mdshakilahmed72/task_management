
from django.contrib import admin
from django.urls import path,include
from users.views import cont


urlpatterns = [
    path('admin/', admin.site.urls),
    path("contact/",cont),
    path("tasks/",include("tasks.urls")),

]
