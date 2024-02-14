from django.urls import path, include

from .views import dies as dies

urlpatterns = [
    path("", dies)
]
