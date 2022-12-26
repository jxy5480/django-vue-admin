from rest_framework.routers import SimpleRouter

from .views import CrudPHModelViewSet

router = SimpleRouter()
router.register("api/crud_ph", CrudPHModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls