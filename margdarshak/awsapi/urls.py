from django.urls import path
from .views import (
    ZoneListCreate, ZoneRetrieveUpdateDestroy,
    AreaListCreate, AreaRetrieveUpdateDestroy,
    ClusterListCreate, ClusterRetrieveUpdateDestroy,
    WLSUListCreate, WLSURetrieveUpdateDestroy,
    CedativeListCreate, CedativeRetrieveUpdateDestroy,
)

urlpatterns = [
    path('zones/', ZoneListCreate.as_view(), name='zone-list'),
    path('zones/<pk>/', ZoneRetrieveUpdateDestroy.as_view(), name='zone-detail'),
    path('areas/', AreaListCreate.as_view(), name='area-list'),
    path('areas/<pk>/', AreaRetrieveUpdateDestroy.as_view(), name='area-detail'),
    path('clusters/', ClusterListCreate.as_view(), name='cluster-list'),
    path('clusters/<pk>/', ClusterRetrieveUpdateDestroy.as_view(), name='cluster-detail'),
    path('wlsus/', WLSUListCreate.as_view(), name='wlsu-list'),
    path('wlsus/<pk>/', WLSURetrieveUpdateDestroy.as_view(), name='wlsu-detail'),
    path('cedatives/', CedativeListCreate.as_view(), name='cedative-list'),
    path('cedatives/<pk>/', CedativeRetrieveUpdateDestroy.as_view(), name='cedative-detail'),
]
