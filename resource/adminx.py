# from django.contrib import admin
from resource.models import ResourceGroups, ExtendResourceInfo, HostResourceInfo, Task

import xadmin

import xadmin.views as xviews


# class ResourceGroupsAdmin(admin.ModelAdmin):
class ResourceGroupsAdmin:
    search_fields = ('name',)
    list_display = ('name', 'created_date', 'modified_date')


xadmin.site.register(ResourceGroups, ResourceGroupsAdmin)


class ExtendResourceInfoAdmin:
    search_fields = ('name',)
    list_display = ('name', 'status', 'resource_group')


xadmin.site.register(ExtendResourceInfo, ExtendResourceInfoAdmin)


class HostResourceInfoAdmin:
    search_fields = ('host_name', 'vips', 'extranet_ips', 'intranet_ips',)
    list_display = ('macs', 'os_type', 'vips', 'extranet_ips', 'intranet_ips',
                    'status', 'memory_size', 'disk_size', 'cpu_num')


xadmin.site.register(HostResourceInfo, HostResourceInfoAdmin)


class TaskAdmin:
    search_fields = ('name', 'status',)
    list_display = ('name', 'crontab', 'is_periodic',
                    'is_deleted', 'status')


xadmin.site.register(Task, TaskAdmin)
