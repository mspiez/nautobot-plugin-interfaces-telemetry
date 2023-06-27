import django_tables2 as tables

from nautobot.dcim.models import Interface
from nautobot.dcim.tables.devices import DeviceComponentTable
from nautobot.apps.tables import BaseTable, ToggleColumn

from nautobot_interfaces_telemetry.models import InterfacesStatus


class InterfacesTelemetryTabTable(BaseTable):
    pk = ToggleColumn()
    interface_name = tables.Column(verbose_name="Name")
    interface_admin_status = tables.Column(verbose_name="Admin Status")
    interface_oper_status = tables.Column(verbose_name="Oper Status")


    def render_interface_name(self, record, column):
        if record.interface_admin_status == record.interface_oper_status:
            column.attrs = {'td': {'bgcolor': 'lightgreen'}}
        else:
            column.attrs = {'td': {'bgcolor': 'orange'}}
        return Interface.objects.get(
            name=record.interface_name, device__name=record.device_name
        )


    def render_interface_admin_status(self, value, record, column):
        
        if record.interface_admin_status == record.interface_oper_status:
            column.attrs = {'td': {'bgcolor': 'lightgreen'}}
        else:
            column.attrs = {'td': {'bgcolor': 'orange'}}
        return value


    def render_interface_oper_status(self, value, record, column):
        
        if record.interface_admin_status == record.interface_oper_status:
            column.attrs = {'td': {'bgcolor': 'lightgreen'}}
        else:
            column.attrs = {'td': {'bgcolor': 'orange'}}
        return value


    class Meta(DeviceComponentTable.Meta):
        model = InterfacesStatus
        fields = (
            "pk",
            "interface_name",
            "interface_admin_status",
            "interface_oper_status",
        )
        default_columns = [
            "pk",
            "interface_name",
            "interface_admin_status",
            "interface_oper_status",
        ]
