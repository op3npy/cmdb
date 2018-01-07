import json

from django.db import models


# todo 参考todo.md ，完善model

class AbstractModel(models.Model):
    # id = models.AutoField(primary_key=True) 默认有
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ResourceGroups(AbstractModel):
    """
    资源组
    """

    name = models.CharField(max_length=300, blank=True, null=True, help_text='组名')

    class Meta:
        managed = False
        db_table = 'resource_groups'


class AbstractResourceModel(AbstractModel):
    """ 抽象资源信息 """
    name = models.CharField(max_length=300, blank=True, null=True, unique=True, help_text='资源名称')
    status = models.IntegerField(blank=True, null=True, help_text='0：正常运行\n'
                                                                  '1停止\n2：删除\n-1：故障')
    comment = models.TextField(blank=True, null=True, help_text='注释信息')
    resource_group = models.ForeignKey(ResourceGroups, on_delete=models.SET_NULL, help_text='资源组')

    class Meta:
        abstract = True


class ExtendResourceInfo(AbstractResourceModel):
    """
    扩展资源信息表， 由自定义扩展
    """
    _types = models.TextField(help_text='存储扩展类型字典', db_column='types')

    @property
    def types(self):
        return json.loads(self._types)

    @types.setter
    def types(self, types):
        self._types = json.dumps(types)

    class Meta:
        managed = False
        db_table = 'extend_resource_info'


class HostResourceInfo(AbstractResourceModel):
    """
    主机资源表， 内置支持物理机，虚拟机，docker容器
    """
    status = models.IntegerField(blank=True, null=True, help_text='0：正常运行\n1：挂起\n2：迁移中(虚拟机和容器有)'
                                                                  '3：下线\n4：关闭\n5：删除\n-1：故障')
    types = models.IntegerField(blank=True, null=True, help_text='资源类型 \n0:物理机\n 1:kvm虚拟机'
                                                                 '2:xen虚拟机\n3:docker容器')
    extranet_ips = models.CharField(max_length=300, null=True, help_text='主机分配的外网ip地址，多个ip以逗号间隔')
    intranet_ips = models.CharField(max_length=300, null=True, help_text='主机分配的内网ip地址，多个ip以逗号间隔')
    vips = models.CharField(max_length=300, null=True, help_text='主机分配的虚拟ip地址，多个ip以逗号间隔')
    macs = models.CharField(max_length=300, null=True, help_text='主机分配的mac地址，多个mac以逗号间隔')
    os_type = models.CharField(max_length=300, null=True, help_text='操作系统类型')
    host_name = models.CharField(max_length=300, null=True, help_text='主机名')
    memory_size = models.FloatField(help_text='内存容量', null=True)
    disk_size = models.FloatField(help_text='磁盘容量', null=True)
    cpu_num = models.FloatField(help_text='cpu核心数', null=True)

    location = models.TextField(help_text='机房内的位置')  # todo ？

    class Meta:
        managed = False
        db_table = 'host_resource_info'


class AbstractHistory(models.Model):
    # todo 如此大量的数据是否需要分表？
    """ 抽象历史记录类，收集主机固定时刻的数据 """
    cpu_usage = models.FloatField(help_text='cpu使用率， 百分比')
    memory_usage = models.FloatField(help_text='内存使用率')
    disk_usage = models.FloatField(help_text='磁盘使用率')
    disk_read_io = models.FloatField(help_text='磁盘读io , 单位byte')
    disk_write_io = models.FloatField(help_text='磁盘写io， 单位byte')
    net_read_io = models.FloatField(help_text='网络下载速度， 单位byte')
    net_write_io = models.FloatField(help_text='网络上传速度， 单位byte')

    class Meta:
        abstract = True


class HistoryVM(AbstractHistory):
    class Meta:
        managed = False
        db_table = 'history_vm'


class HistoryHost(AbstractHistory):
    class Meta:
        managed = False
        db_table = 'history_host'


class HistoryContainer(AbstractHistory):
    class Meta:
        managed = False
        db_table = 'history_container'


class Task(AbstractModel):
    status = models.IntegerField(blank=True, null=True)
    main = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'
