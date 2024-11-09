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
from dcim.models import (
    DeviceRole,
    DeviceType,
    Location,
    Platform,
    Region,
    Site,
    SiteGroup,
)

from netbox_os_manager.models.goldenimage import *
from netbox_os_manager.models.image import *

__all__ = ["GoldenImageForm"]

# ==============================================================================
# Forms
# ==============================================================================


class GoldenImageForm(NetBoxModelForm):

    image = DynamicModelChoiceField(
        queryset=Image.objects.all(),
        label="Image",
        help_text="Chose software image which you want to select as golden image",
        required=True,
    )

    regions = DynamicModelMultipleChoiceField(
        label="Regions", queryset=Region.objects.all(), required=False
    )

    site_groups = DynamicModelMultipleChoiceField(
        label="Site groups", queryset=SiteGroup.objects.all(), required=False
    )

    sites = DynamicModelMultipleChoiceField(
        label="Sites", queryset=Site.objects.all(), required=False
    )

    locations = DynamicModelMultipleChoiceField(
        label="Locations", queryset=Location.objects.all(), required=False
    )

    device_types = DynamicModelMultipleChoiceField(
        label="Device types", queryset=DeviceType.objects.all(), required=False
    )

    roles = DynamicModelMultipleChoiceField(
        label="Roles", queryset=DeviceRole.objects.all(), required=False
    )

    platforms = DynamicModelMultipleChoiceField(
        label="Platforms", queryset=Platform.objects.all(), required=False
    )

    comments = CommentField()

    class Meta:
        model = GoldenImage
        fields = (
            "name",
            "image",
            "description",
            "regions",
            "site_groups",
            "sites",
            "locations",
            "device_types",
            "roles",
            "platforms",
            "comments",
        )
