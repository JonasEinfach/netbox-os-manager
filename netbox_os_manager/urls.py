# ==============================================================================
# Imports
# ==============================================================================

from django.urls import path

# Views for changelog
from netbox.views.generic import ObjectChangeLogView

# ==============================================================================
# Special Model Imports
# ==============================================================================

from .models import (
    Image,
    GoldenImage,
    ImageDistributionServer,
    SettingsDeviceType,
)

from .views import (
    ImageView,
    ImageListView,
    ImageEditView,
    ImageDeleteView,
    GoldenImageView,
    GoldenImageListView,
    GoldenImageEditView,
    GoldenImageDeleteView,
    ImageDistributionServerView,
    ImageDistributionServerListView,
    ImageDistributionServerEditView,
    ImageDistributionServerDeleteView,
    SettingsDeviceTypeView,
    SettingsDeviceTypeListView,
    SettingsDeviceTypeEditView,
    SettingsDeviceTypeDeleteView,
)

# ==============================================================================
# Global Variables
# ==============================================================================

# ==============================================================================
# Urls
# ==============================================================================

# fmt: off

urlpatterns = (
    
    # Images
    path("images/", ImageListView.as_view(), name="image_list"),
    path("images/add/", ImageEditView.as_view(), name="image_add"),
    path("images/<int:pk>/", ImageView.as_view(), name="image"),
    path("images/<int:pk>/edit/", ImageEditView.as_view(), name="image_edit"),
    path("images/<int:pk>/delete/", ImageDeleteView.as_view(), name="image_delete"),
    path('images/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='image_changelog', kwargs={
        'model': Image
    }),

    # GoldenImages
    path("goldenimages/", GoldenImageListView.as_view(), name="goldenimage_list"),
    path("goldenimages/add/", GoldenImageEditView.as_view(), name="goldenimage_add"),
    path("goldenimages/<int:pk>/", GoldenImageView.as_view(), name="goldenimage"),
    path("goldenimages/<int:pk>/edit/", GoldenImageEditView.as_view(), name="goldenimage_edit"),
    path("goldenimages/<int:pk>/delete/",GoldenImageDeleteView.as_view(),name="goldenimage_delete"),
    path('goldenimages/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='goldenimage_changelog', kwargs={
        'model': GoldenImage
    }),
    
    # ImageDistributionServers
    path("imagedistributionservers/", ImageDistributionServerListView.as_view(), name="imagedistributionserver_list"),
    path("imagedistributionservers/add/", ImageDistributionServerEditView.as_view(), name="imagedistributionserver_add"),
    path("imagedistributionservers/<int:pk>/", ImageDistributionServerView.as_view(), name="imagedistributionserver"),
    path("imagedistributionservers/<int:pk>/edit/", ImageDistributionServerEditView.as_view(), name="imagedistributionserver_edit"),
    path("imagedistributionservers/<int:pk>/delete/",ImageDistributionServerDeleteView.as_view(),name="imagedistributionserver_delete"),
    path('imagedistributionservers/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='imagedistributionserver_changelog', kwargs={
        'model': ImageDistributionServer
    }),

    # SettingsDeviceTypes
    path("settingsdevicetypes/", SettingsDeviceTypeListView.as_view(), name="settingsdevicetype_list"),
    path("settingsdevicetypes/add/", SettingsDeviceTypeEditView.as_view(), name="settingsdevicetype_add"),
    path("settingsdevicetypes/<int:pk>/", SettingsDeviceTypeView.as_view(), name="settingsdevicetype"),
    path("settingsdevicetypes/<int:pk>/edit/", SettingsDeviceTypeEditView.as_view(), name="settingsdevicetype_edit"),
    path("settingsdevicetypes/<int:pk>/delete/",SettingsDeviceTypeDeleteView.as_view(),name="settingsdevicetype_delete"),
    path('settingsdevicetypes/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='settingsdevicetype_changelog', kwargs={
        'model': SettingsDeviceType
    }),
)

# fmt: on
