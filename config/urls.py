from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from dataset_api.views import DataViewSet


router = SimpleRouter()
router.register(r'api', DataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
