from django.urls import path

from nautobot_interfaces_telemetry import views

urlpatterns = [
    path(
        "devices/<uuid:pk>/",
        views.DeviceInterfacesStatusTab.as_view(),
        name="interfacestelemetry_tab",
    ),
]
