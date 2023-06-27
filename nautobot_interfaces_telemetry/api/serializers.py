from rest_framework import serializers

from nautobot.apps.api import NautobotModelSerializer

from nautobot_interfaces_telemetry.models import InterfacesStatus


class InterfacesStatusSerializer(NautobotModelSerializer):
    """API serializer for interacting with InterfacesStatus objects."""

    interface_id = serializers.CharField(required=False)
    device_id = serializers.CharField(required=False)

    class Meta:
        model = InterfacesStatus
        fields = [
            "id",
            "interface_admin_status",
            "interface_oper_status",
            "interface_name",
            "device_name",
            "interface_id",
            "device_id",
            "slug",
        ]
