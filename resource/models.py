from django.db import models


# todo 参考todo.md ，完善model

class AbstractModel(models.Model):
    id = models.IntegerField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ResourceGroups(AbstractModel):
    """
    资源组
    """

    name = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_groups'


class ResourceInfo(AbstractModel):
    """
    资源表
    """

    name = models.CharField(max_length=300, blank=True, null=True)
    ips = models.CharField(max_length=300, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    types = models.IntegerField(blank=True, null=True)
    group_id = models.ForeignKey(ResourceGroups, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'resource_info'


class Task(AbstractModel):
    status = models.IntegerField(blank=True, null=True)
    main = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'
