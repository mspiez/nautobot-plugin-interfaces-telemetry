from importlib import metadata

__version__ = metadata.version(__name__)


from nautobot.apps import NautobotAppConfig


class InterfacesTelemetryAppConfig(NautobotAppConfig):
    name = "nautobot_interfaces_telemetry"
    verbose_name = "Interfaces Telemetry"
    description = "A POC plugin that shows interfaces status"
    version = "0.0.2"
    author = "Michal Spiez"
    author_email = "mspiez@gmail.com"
    base_url = "interfaces-telemetry"
    required_settings = []
    default_settings = {"loud": False}


config = InterfacesTelemetryAppConfig
