# ==============================================================================
# Imports
# ==============================================================================

from netbox.jobs import JobRunner

# ==============================================================================
# Jobs
# ==============================================================================

"""
Help:

Documentation:
https://github.com/netbox-community/netbox/blob/1e5f79a8ed8f046ce70c0bfb2859fb72a347133d/docs/plugins/development/background-jobs.md

Examples:
https://github.com/renatoalmeidaoliveira/nbrobot/blob/main/nb_robot/jobs.py
https://github.com/netboxlabs/netbox-branching/blob/develop/netbox_branching/jobs.py
https://github.com/DanSheps/netbox-config-backup/blob/master/netbox_config_backup/jobs/backup.py

https://github.com/netbox-community/netbox/discussions/14040

"""


class OSManagerJob(JobRunner):

    class Meta:
        name = "OSManagerJob"
