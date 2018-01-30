# cmdb
运维管理平台
* resource it资源管理系统，包括物理机，虚拟机，容器等等，具有扩展功能，
可以编写扩展监控指定的资源，比如ssh服务，数据库服务等软件和硬件资源。
支持任务调度，如自动部署
* webterminal web终端系统，堡垒机。针对linux shell（支持rs/sz） 和windows rdp
* agent 是客户端监控代理，跨平台，暂时和web端放在一起，发布的时候分离开，
agent本地采用sqlite存储，与服务器交互采用websocket协议
https://channels.readthedocs.io/en/latest/getting-started.html
* sso 单点登陆系统。内部的应用可以使用此系统做统一服务 （依靠django 第三方sso库，添加业务代码）
* audit 审计系统。
* 安全中心 （非重点）， 需要单独开发监控系统，部署在网关，
包括流量分析（web攻击，ddos攻击，暴力破解），安全态势，漏洞管理，
以及设备监控（非法媒介挂载到物理机，非法设备入网）、高危操作监控。参考蜜獾系统http://www.4hou.com/technology/9687.html 和
安全运维http://www.freebuf.com/articles/neopoints/158586.html
DNSlog http://www.polaris-lab.com/index.php/archives/423/


公用系统
* 日志系统
* 告警系统 （邮箱，短信，应用内）
* 报表系统
* 任务管理系统 ？

*开发注意事项*
* 历史记录和日志等采用InfluxDB数据库https://github.com/bitlabstudio/django-influxdb-metrics
* 开发数据伪造功能为应用提供假数据
* 单元测试必须完备
* 功能测试
* 所有敏感数据都从环境变量获取
* 服务器只能打开特定端口，其它默认屏蔽

参考：
* https://github.com/jumpserver/jumpserver
* https://github.com/nigma/django-request-id