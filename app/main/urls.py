from django.urls import path, include
from rest_framework import routers
from drf import views as drf_views

router = routers.DefaultRouter()
router.register(r'users', drf_views.User_Viewset)
router.register(r'groups', drf_views.Group_Viewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]