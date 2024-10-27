# ==============================================================================
# Imports
# ==============================================================================

# plugin menu imports
from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem

# import for menu buttons
from netbox.choices import ButtonColorChoices

# ==============================================================================
# PluginMenuItems
# ==============================================================================

menuitemimages = PluginMenuItem(
    link="plugins:netbox_os_manager:image_list",
    link_text="Images",
    buttons=(
        PluginMenuButton(
            "plugins:netbox_os_manager:image_add",
            "Add",
            "mdi mdi-plus-thick",
        ),
    ),
)

menuitemgoldenimages = PluginMenuItem(
    link="plugins:netbox_os_manager:goldenimage_list",
    link_text="Golden Images",
    buttons=(
        PluginMenuButton(
            "plugins:netbox_os_manager:goldenimage_add",
            "Add",
            "mdi mdi-plus-thick",
        ),
    ),
)

menuitemimagedistributionservers = PluginMenuItem(
    link="plugins:netbox_os_manager:imagedistributionserver_list",
    link_text="Image Distribution Servers",
    buttons=(
        PluginMenuButton(
            "plugins:netbox_os_manager:imagedistributionserver_add",
            "Add",
            "mdi mdi-plus-thick",
        ),
    ),
)

menuitemsettingsdevicetype = PluginMenuItem(
    link="plugins:netbox_os_manager:settingsdevicetype_list",
    link_text="Settings Device Types",
    buttons=(
        PluginMenuButton(
            "plugins:netbox_os_manager:settingsdevicetype_add",
            "Add",
            "mdi mdi-plus-thick",
        ),
    ),
)

# ==============================================================================
# PluginMenu
# ==============================================================================

menu = PluginMenu(
    label="OS - Manager",
    groups=(
        (
            "Images",
            (
                menuitemimages,
                menuitemgoldenimages,
            ),
        ),
        (
            "Settings",
            (
                menuitemimagedistributionservers,
                menuitemsettingsdevicetype,
            ),
        ),
    ),
    icon_class="mdi mdi-autorenew",
)
