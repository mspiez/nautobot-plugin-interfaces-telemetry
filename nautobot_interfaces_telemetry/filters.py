import django_filters

from nautobot.dcim.models import Interface
from nautobot.apps.filters import BaseFilterSet, MultiValueCharFilter

from nautobot_interfaces_telemetry.models import InterfacesStatus


class InterfaceStatustFilterSet(BaseFilterSet):
    interface_admin_status = django_filters.ModelMultipleChoiceFilter(
        queryset=InterfacesStatus.objects.all(),
        field_name="interface_admin_status",
        label="Interface Admin Status",
    )

    interface_oper_status = django_filters.ModelMultipleChoiceFilter(
        queryset=InterfacesStatus.objects.all(),
        field_name="interface_oper_status",
        label="Interface Oper Status",
    )

    interface_id = MultiValueCharFilter(
        method="filter_by_interface_id", field_name="id", label="Interface ID"
    )
    device_id = django_filters.ModelMultipleChoiceFilter(
        queryset=InterfacesStatus.objects.all(),
        field_name="device_id",
        label="Device ID",
    )

    def filter_by_interface_id(self, queryset, name, value):
        try:
            ifaces = Interface.objects.filter(id__in=value)
        except (Interface.DoesNotExist, Interface.MultipleObjectsReturned):
            return queryset
        interfaces_names = [iface.name for iface in ifaces]
        devices_names = [iface.device.name for iface in ifaces if iface.device]

        return queryset.filter(
            interface_name__in=interfaces_names, device_name__in=devices_names
        )

    class Meta:
        model = InterfacesStatus
        fields = [
            "interface_admin_status",
            "interface_oper_status",
            "interface_id",
            "device_id",
        ]
