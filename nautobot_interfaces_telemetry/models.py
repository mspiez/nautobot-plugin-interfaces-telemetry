import uuid
from django.db import models

from django.utils.text import slugify
from typing import Optional
from django.core.exceptions import ValidationError


from nautobot.core.fields import AutoSlugField
from nautobot.apps.models import OrganizationalModel
from nautobot.dcim.models import Device
from nautobot.dcim.models import Interface
from nautobot.extras.utils import extras_features


@extras_features(
    "custom_fields",
    "relationships",
)
class InterfacesStatus(OrganizationalModel):
    """Base model for Interface Status"""

    interface_admin_status = models.CharField(max_length=50, blank=True)
    interface_oper_status = models.CharField(max_length=50)
    interface_name = models.CharField(max_length=50)
    device_name = models.CharField(max_length=50)
    slug = AutoSlugField(
        populate_from=("device_name", "interface_name"), separator="__"
    )

    @property
    def interface_id(self) -> Optional[uuid.uuid4]:
        try:
            interface = Interface.objects.get(
                name=self.interface_name, device__name=self.device_name
            )
        except Interface.DoesNotExists:
            return None
        return interface.id

    @property
    def device_id(self) -> Optional[uuid.uuid4]:
        try:
            device = Device.objects.get(name=self.device_name)
        except Interface.DoesNotExists:
            return None
        return device.id

    def __str__(self):
        return self.slug

    def clean(self):
        if not self.slug:
            return
        new_slug = slugify(f"{self.device_name}__{self.interface_name}")
        if new_slug != self.slug:
            raise ValidationError(
                f"Device name or interface name attributes should not be modified. New slug {new_slug} does not match existing one: {self.slug}"
            )

    class Meta:
        unique_together = (
            "interface_name",
            "device_name",
        )
