from django.contrib import admin
from resource.models import ResourceGroups, ExtendResourceInfo, HostResourceInfo, Task


# todo 不使用， 采用crud

@admin.register(ResourceGroups)
class ResourceGroupsAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(ExtendResourceInfo)
class ExtendResourceInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(HostResourceInfo)
class HostResourceInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
