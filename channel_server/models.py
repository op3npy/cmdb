from django.db import models


class AbstractListModel(models.Model):
    # id = models.AutoField(primary_key=True) 默认有
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    ip_address = models.TextField(max_length=40, help_text='存储ip地址或者CIDR 网段')

    class Meta:
        abstract = True


class BlackList(AbstractListModel):
    """
    黑名单
    """

    class Meta:
        db_table = 'black_list'


class WhiteList(AbstractListModel):
    """
    白名单
    """

    class Meta:
        db_table = 'white_list'
