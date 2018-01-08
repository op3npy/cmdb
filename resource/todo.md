resource it资源管理系统，包括物理机，虚拟机，容器等等，具有扩展功能，
可以编写扩展监控指定的资源，比如ssh服务，数据库服务等软件和硬件资源。
支持任务调度，如自动部署

* 实现物理机，虚拟机，容器 这三类资源的监控（磁盘容量，内存，cpu，网络）
* 资源扩展操作插件的接口定义，提供插件编写模板。
扩展比如：目录大小监控，服务监控
软件资源也可以发送心跳包以告诉服务器最新状态
* 资源和资源组的增删改查，指定资源或者资源组特定任务执行
* 定时任务模块（写入数据库 or celery + rabbitmq/redis ?）
* 资源数据导入，模板下载
* 和agent保持长连接，由agent发送心跳包
* agent端要有配置和脚本下发记录，数据发送记录

数据库设计参考
> http://www.cnblogs.com/jcpythoner/p/cmdb.html
> http://autohomeops.corpautohome.com/articles/%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6CMDB%E8%AE%BE%E8%AE%A1%E6%80%9D%E8%B7%AF/
> http://dbaplus.cn/news-21-1271-1.html