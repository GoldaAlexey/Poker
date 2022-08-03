from urllib.parse import urlparse
from django.urls import path

from . import views

urlpatterns = [
    path("tables/", views.TableListView.as_view()),
    path("tables/<int:pk>/", views.TableView.as_view()),
    path("tables/CreateTable/", views.TableView.as_view()),
]