"""Defines scoreboard URLs"""
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'credentials', views.CredentialViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('credentials', views.credentials, name='credentials'),
    path('services', views.services, name='services'),
    # path('mickey', views.mickey, name='mickey'),
    # path('api/credentials', views.CredentialViewSet.as_view(), name='credentials_api'),
    # path('api/scores', views.TheFunction, name='scores_api')
    path('api/', include(router.urls))
]

urlpatterns += router.urls
