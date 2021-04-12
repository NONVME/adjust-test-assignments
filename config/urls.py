from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from dataset_api.views import DataViewSet, import_dataset

router = SimpleRouter()
router.register(r'api', DataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('upload/', import_dataset),
]
