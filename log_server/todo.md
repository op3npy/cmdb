

可部署在独立的日志服务器上

* 日志的备份，可配置专门的日志存储服务器
* 主动采集： 日志采集（包括全链路日志获取），日志路径配置
* 被动采集：
* 日志搜索
* 可视化展示（图表展示样式可选）
* 日志规则，提供内置（仅管理员角色有操作内置规则的权限）
* influxdb 或者 rsyslog/syslog-ng + sentry/
https://pythonhosted.org/loggerglue/gettingstarted.html
* 日志全文搜索http://blog.csdn.net/ac_hell/article/details/52875927
http://django-haystack.readthedocs.io/en/master/tutorial.html
用python实现windows和linux下syslog客户端（conf文件生成， conf格式检查）
https://www.jianshu.com/p/8656fc85e497
* linux日志文件http://blog.csdn.net/oxford_d/article/details/51820031
* 提供高级sql查询？




设计参考
>https://tech.meituan.com/satellite_system.html
https://linux.cn/article-5023-1.html
[python syslog_client logging.handlers.SysLogHandler](https://docs.python.org/2/library/logging.handlers.html)


