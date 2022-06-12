from django.urls import path
from . import views

urlpatterns = [
    # Author Url
    path('<str:pk>', views.index, name="author"),
]
