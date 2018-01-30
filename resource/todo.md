
resource it资源管理系统，包括物理机，虚拟机，容器等等，具有扩展功能，
可以编写扩展监控指定的资源，比如ssh服务，数据库服务等软件和硬件资源。
支持任务调度，如自动部署

* 实现物理机，虚拟机，容器 这三类资源的监控（磁盘容量，内存，cpu，网络）
* 资源扩展操作插件的接口定义，提供插件编写模板。
扩展比如：目录大小监控，服务监控，
软件资源也可以发送心跳包以告诉服务器最新状态
* 资源和资源组的增删改查，指定资源或者资源组特定任务执行
* 定时任务模块（写入数据库 并且交由celery + rabbitmq/redis ? 执行调度）
包括名词（唯一）、间隔时间、指定时间点执行、是否重复、脚本类型（文本文件类型，支持python，shell等实现规定的输入输出，并且客户端支持则可以，默认python，此字段可以在前端实现简单的ide功能）、指定参数、ctime, atime
* 资源数据导入，模板下载
* 和agent保持长连接，由agent发送心跳包 http://channels.readthedocs.io/en/stable/getting-started.html
* agent端要有配置、脚本下发、脚本执行、执行结果的记录，数据发送记录，服务器端主动执行采用fabric，前提是ssh密钥配置好
* 主动采集和被动采集
* 时间序列数据的可视化
* 客户端ssh用户名密码存储，服务器公钥分发

数据库设计参考
> http://www.cnblogs.com/jcpythoner/p/cmdb.html
> http://autohomeops.corpautohome.com/articles/%E6%B1%BD%E8%BD%A6%E4%B9%8B%E5%AE%B6CMDB%E8%AE%BE%E8%AE%A1%E6%80%9D%E8%B7%AF/
> http://dbaplus.cn/news-21-1271-1.html