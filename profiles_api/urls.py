from django.urls import path
from profiles_api import views


urlpatterns =[
    path('hello-view/',views.HelloApiView.as_view()), #https://127.0.0.1:8000/api/hello-view/ will route you here to this
]
