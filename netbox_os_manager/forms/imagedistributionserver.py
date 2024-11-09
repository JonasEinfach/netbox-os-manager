# ==============================================================================
# Imports
# ==============================================================================

from netbox.forms import NetBoxModelForm, NetBoxModelBulkEditForm
from django import forms
from utilities.forms.fields import (
    CommentField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
)
from utilities.forms.rendering import FieldSet

# Custom stuff
from ipam.models import IPAddress

from netbox_os_manager.models.imagedistributionserver import *

__all__ = ["ImageDistributionServerForm"]

# ==============================================================================
# Forms
# ==============================================================================


class ImageDistributionServerForm(NetBoxModelForm):

    ip = DynamicModelChoiceField(
        queryset=IPAddress.objects.all(),
        label="IP",
        help_text="Chose ip address of image distribution server",
        required=True,
    )

    comments = CommentField()

    class Meta:
        model = ImageDistributionServer
        fields = (
            "ip",
            "name",
            "description",
            "download_method",
            "custom_port",
            "comments",
        )
