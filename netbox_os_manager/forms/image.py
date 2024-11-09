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

from netbox_os_manager.models.image import *

__all__ = ["ImageForm"]

# ==============================================================================
# Forms
# ==============================================================================


class ImageForm(NetBoxModelForm):

    image = forms.FileField(
        required=True,
        label="Image",
        help_text="Image File, with .bin extension",
    )

    md5sum = forms.CharField(
        required=True,
        label="MD5 Checksum",
        help_text="Expected MD5 Checksum, ex: 0f58a02f3d3f1e1be8f509d2e5b58fb8",
    )

    version = forms.CharField(
        required=True,
        label="Version",
        help_text="Verbose Software Version, ex: 17.9.3",
    )

    comments = CommentField()

    class Meta:
        model = Image
        fields = (
            "image",
            "md5sum",
            "version",
            "description",
            "comments",
            "tags",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # If a image is uploaded, no image file change is allowed!
        if self.instance.image_exists:
            self.fields["image"].widget.attrs["disabled"] = True
            self.fields["image"].initial = self.instance.image
            self.fields["image"].help_text = "Image File can't be changed!"
