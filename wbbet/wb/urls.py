from .views import WildberriesViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('action', WildberriesViewSet, basename='wildberries')

urlpatterns = router.urls
