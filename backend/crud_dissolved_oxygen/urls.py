from rest_framework.routers import SimpleRouter

from .views import CrudDissolvedOxygenModelViewSet

router = SimpleRouter()
router.register("api/crud_dissolved_oxygen", CrudDissolvedOxygenModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls