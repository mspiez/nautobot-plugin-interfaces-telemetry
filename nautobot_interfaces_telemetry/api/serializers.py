from rest_framework import serializers

from nautobot.apps.api import NautobotModelSerializer

from nautobot_interfaces_telemetry.models import InterfacesStatus


class InterfacesStatusSerializer(NautobotModelSerializer):
    """API serializer for interacting with InterfacesStatus objects."""

    interface_id = serializers.CharField(required=False)
    device_id = serializers.CharField(required=False)

    # >>> from nautobot.core.utils.lookup import get_route_for_model
    # >>> get_route_for_model(InterfacesStatus, "list", api=True)
    # 'plugins-api:nautobot_interfaces_telemetry-api:interfacesstatus-list'
    # >>> 
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:nautobot_interfaces_telemetry-api:interfacesstatus-detail", lookup_field="slug")

    class Meta:
        model = InterfacesStatus
        fields = "__all__"
