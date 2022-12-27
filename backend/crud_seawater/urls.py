from rest_framework.routers import SimpleRouter

from .views import CrudSeawaterModelViewSet

router = SimpleRouter()
router.register("api/crud_seawater", CrudSeawaterModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls