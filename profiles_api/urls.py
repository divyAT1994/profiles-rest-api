from django.urls import path, include
from profiles_api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name='hello-viewset')
router.register('profile-viewset',views.UserProfileViewSet)

urlpatterns =[
    path('hello-view/',views.HelloApiView.as_view()), #https://127.0.0.1:8000/api/hello-view/ will route you here to this
    path('',include(router.urls))
]
