from main.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', TaskViewSet, basename='task')

urlpatterns = []

urlpatterns += router.urls