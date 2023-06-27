from nautobot.apps.api import NautobotModelViewSet

from nautobot_interfaces_telemetry.api.serializers import InterfacesStatusSerializer
from nautobot_interfaces_telemetry.models import InterfacesStatus
from nautobot_interfaces_telemetry.filters import InterfaceStatustFilterSet


class InterfacesStatusViewSet(NautobotModelViewSet):
    """API viewset for interacting with InterfacesStatus objects."""

    queryset = InterfacesStatus.objects.all()
    serializer_class = InterfacesStatusSerializer
    filterset_class = InterfaceStatustFilterSet

    lookup_field = "slug"
