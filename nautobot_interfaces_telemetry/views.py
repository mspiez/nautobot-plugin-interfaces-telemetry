from nautobot.apps import views
from nautobot.dcim.models import Device

from nautobot_interfaces_telemetry.models import InterfacesStatus
from nautobot_interfaces_telemetry.tables import InterfacesTelemetryTabTable


class DeviceInterfacesStatusTab(views.ObjectView):
    queryset = Device.objects.all()
    template_name = "nautobot_interfaces_telemetry/interfaces_telemetry.html"

    def get_extra_context(self, request, instance):
        interfaces_table = InterfacesTelemetryTabTable(
            data=InterfacesStatus.objects.filter(device_name=instance.name),
            user=request.user,
            orderable=False,
        )

        return {
            "interfaces_table": interfaces_table,
            "active_tab": "interfaces-telemetry",
        }
