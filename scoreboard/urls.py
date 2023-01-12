"""Defines scoreboard URLs"""
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as drf_views
from . import views

router = routers.DefaultRouter()
router.register(r'credentials', views.CredentialViewSet)
router.register(r'scores', views.ScoreViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('credentials', views.credentials, name='credentials'),
    path('services', views.services, name='services'),
    # path('mickey', views.mickey, name='mickey'),
    # path('api/credentials', views.CredentialViewSet.as_view(), name='credentials_api'),
    # path('api/scores', views.TheFunction, name='scores_api')
    path('api/', include(router.urls)),
    path('api/get-token', drf_views.obtain_auth_token)
]

urlpatterns += router.urls
