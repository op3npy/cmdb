# from django.contrib import admin
import xadmin

from resource.models import ResourceGroups, ExtendResourceInfo, HostResourceInfo, Task


class ResourceGroupsAdmin:
    search_fields = ('name',)
    list_display = ('name', 'created_date', 'modified_date')


class ExtendResourceInfoAdmin:
    search_fields = ('name',)
    list_display = ('name', 'status', 'resource_group')


class HostResourceInfoAdmin:
    search_fields = ('host_name', 'vips', 'extranet_ips', 'intranet_ips',)
    list_display = ('macs', 'os_type', 'vips', 'extranet_ips', 'intranet_ips',
                    'status', 'memory_size', 'disk_size', 'cpu_num')


class TaskAdmin:
    search_fields = ('name', 'status',)
    list_display = ('name', 'crontab', 'is_periodic',
                    'is_deleted', 'status')


xadmin.site.register(ResourceGroups, ResourceGroupsAdmin)
xadmin.site.register(ExtendResourceInfo, ExtendResourceInfoAdmin)
xadmin.site.register(HostResourceInfo, HostResourceInfoAdmin)
xadmin.site.register(Task, TaskAdmin)
