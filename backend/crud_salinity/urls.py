from rest_framework.routers import SimpleRouter

from .views import CrudSalinityModelViewSet

router = SimpleRouter()
router.register("api/crud_salinity", CrudSalinityModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls