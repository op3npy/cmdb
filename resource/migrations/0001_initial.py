# Generated by Django 2.0.1 on 2018-01-16 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryVM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_usage', models.FloatField(help_text='cpu使用率， 百分比')),
                ('memory_usage', models.FloatField(help_text='内存使用率')),
                ('disk_usage', models.FloatField(help_text='磁盘使用率')),
                ('disk_read_io', models.FloatField(help_text='磁盘读io , 单位byte')),
                ('disk_write_io', models.FloatField(help_text='磁盘写io， 单位byte')),
                ('net_read_io', models.FloatField(help_text='网络下载速度， 单位byte')),
                ('net_write_io', models.FloatField(help_text='网络上传速度， 单位byte')),
                ('collecting_time', models.DateTimeField(help_text='采集时间')),
            ],
            options={
                'db_table': 'history_vm',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExtendResourceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, help_text='资源名称', max_length=255, null=True, unique=True)),
                ('status', models.IntegerField(blank=True, help_text='0：正常运行\n1停止\n2：删除\n-1：故障', null=True)),
                ('comment', models.TextField(blank=True, help_text='注释信息', null=True)),
                ('_types', models.TextField(db_column='types', help_text='存储扩展类型字典')),
            ],
            options={
                'db_table': 'extend_resource_info',
            },
        ),
        migrations.CreateModel(
            name='HistoryContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_usage', models.FloatField(help_text='cpu使用率， 百分比')),
                ('memory_usage', models.FloatField(help_text='内存使用率')),
                ('disk_usage', models.FloatField(help_text='磁盘使用率')),
                ('disk_read_io', models.FloatField(help_text='磁盘读io , 单位byte')),
                ('disk_write_io', models.FloatField(help_text='磁盘写io， 单位byte')),
                ('net_read_io', models.FloatField(help_text='网络下载速度， 单位byte')),
                ('net_write_io', models.FloatField(help_text='网络上传速度， 单位byte')),
                ('collecting_time', models.DateTimeField(help_text='采集时间')),
            ],
            options={
                'db_table': 'history_container',
            },
        ),
        migrations.CreateModel(
            name='HistoryHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_usage', models.FloatField(help_text='cpu使用率， 百分比')),
                ('memory_usage', models.FloatField(help_text='内存使用率')),
                ('disk_usage', models.FloatField(help_text='磁盘使用率')),
                ('disk_read_io', models.FloatField(help_text='磁盘读io , 单位byte')),
                ('disk_write_io', models.FloatField(help_text='磁盘写io， 单位byte')),
                ('net_read_io', models.FloatField(help_text='网络下载速度， 单位byte')),
                ('net_write_io', models.FloatField(help_text='网络上传速度， 单位byte')),
                ('collecting_time', models.DateTimeField(help_text='采集时间')),
            ],
            options={
                'db_table': 'history_host',
            },
        ),
        migrations.CreateModel(
            name='HostResourceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, help_text='资源名称', max_length=255, null=True, unique=True)),
                ('comment', models.TextField(blank=True, help_text='注释信息', null=True)),
                ('status', models.IntegerField(blank=True, help_text='0：正常运行\n1：挂起\n2：迁移中(虚拟机和容器有)3：下线\n4：关闭\n5：删除\n-1：故障', null=True)),
                ('types', models.IntegerField(blank=True, help_text='资源类型 \n0:物理机\n 1:kvm虚拟机2:xen虚拟机\n3:docker容器', null=True)),
                ('extranet_ips', models.CharField(help_text='主机分配的外网ip地址，多个ip以逗号间隔', max_length=300, null=True)),
                ('intranet_ips', models.CharField(help_text='主机分配的内网ip地址，多个ip以逗号间隔', max_length=300, null=True)),
                ('vips', models.CharField(help_text='主机分配的虚拟ip地址，多个ip以逗号间隔', max_length=300, null=True)),
                ('macs', models.CharField(help_text='主机分配的mac地址，多个mac以逗号间隔', max_length=300, null=True)),
                ('os_type', models.CharField(help_text='操作系统类型', max_length=300, null=True)),
                ('host_name', models.CharField(help_text='主机名', max_length=300, null=True)),
                ('memory_size', models.FloatField(help_text='内存容量', null=True)),
                ('disk_size', models.FloatField(help_text='磁盘容量', null=True)),
                ('cpu_num', models.FloatField(help_text='cpu核心数', null=True)),
                ('location', models.TextField(help_text='机房内的位置')),
            ],
            options={
                'db_table': 'host_resource_info',
            },
        ),
        migrations.CreateModel(
            name='ResourceGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, help_text='组名', max_length=300, null=True)),
            ],
            options={
                'db_table': 'resource_groups',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('main', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.AddField(
            model_name='hostresourceinfo',
            name='resource_group',
            field=models.ForeignKey(help_text='资源组', null=True, on_delete=django.db.models.deletion.SET_NULL, to='resource.ResourceGroups'),
        ),
        migrations.AddField(
            model_name='extendresourceinfo',
            name='resource_group',
            field=models.ForeignKey(help_text='资源组', null=True, on_delete=django.db.models.deletion.SET_NULL, to='resource.ResourceGroups'),
        ),
    ]
