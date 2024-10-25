from netbox.plugins import PluginConfig


class NetBoxOSManagerConfig(PluginConfig):
    name = 'netbox_os_manager'
    verbose_name = 'NetBox OS Manager'
    description = 'Netbox plugin to manage operating systems on your network devices.'
    author: str = "Jonas Einfach"
    author_email: str = "jonaseinfachgithub@gmail.de"
    version = '0.1.0'
    base_url = 'os-manager'

    queues = ['task_executer']


config = NetBoxOSManagerConfig
