from django.contrib import admin

from nautobot.apps.admin import NautobotModelAdmin

from nautobot_interfaces_telemetry.models import InterfacesStatus


@admin.register(InterfacesStatus)
class InterfaceStatusAdmin(NautobotModelAdmin):
    list_display = (
        "interface_admin_status",
        "interface_oper_status",
        "interface_name",
        "device_name",
        "slug",
    )
