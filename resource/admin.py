from django.contrib import admin
from resource.models import ResourceGroups, ExtendResourceInfo, HostResourceInfo, Task


# todo 不使用， 采用crud

@admin.register(ResourceGroups)
class ResourceGroupsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'created_date', 'modified_date')

@admin.register(ExtendResourceInfo)
class ExtendResourceInfoAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'status', 'resource_group')


@admin.register(HostResourceInfo)
class HostResourceInfoAdmin(admin.ModelAdmin):
    search_fields = ('host_name', 'vips', 'extranet_ips', 'intranet_ips',)
    list_display = ('macs','os_type','vips', 'extranet_ips','intranet_ips',
                    'status', 'memory_size', 'disk_size','cpu_num')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ('name', 'status', )
    list_display = ('name', 'crontab', 'is_periodic',
                    'is_deleted', 'status')
