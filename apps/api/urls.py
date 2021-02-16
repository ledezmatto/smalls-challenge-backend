from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.api.views import *

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('post-fav/', PostViewSet.as_view()),
    path('check-fav/<str:pk>/', PostFavViewSet.as_view()),
    path('unfav-allposts/', UnFavAllPostViewSet.as_view()),
]