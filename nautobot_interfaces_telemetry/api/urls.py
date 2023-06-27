from nautobot.apps.api import OrderedDefaultRouter
from nautobot_interfaces_telemetry.api.views import InterfacesStatusViewSet


router = OrderedDefaultRouter()
router.register("interfaces-status", InterfacesStatusViewSet)

urlpatterns = router.urls
