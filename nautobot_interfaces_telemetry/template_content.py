from django.urls import reverse
from nautobot.apps.ui import TemplateExtension


class DeviceExtraTab(TemplateExtension):
    """Template extension to add extra tabs to the object detail tabs."""

    model = "dcim.device"

    def detail_tabs(self):
        return [
            {
                "title": "Interfaces Telemetry",
                "url": reverse(
                    "plugins:nautobot_interfaces_telemetry:interfacestelemetry_tab",
                    kwargs={"pk": self.context["object"].pk},
                ),
            }
        ]


template_extensions = [DeviceExtraTab]
