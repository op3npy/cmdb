# cmdb
运维管理平台

agent 是客户端，为了简便，不单独再起提供项目，暂时和web端放在一起，发布的时候分离开
agent本地采用sqlite存储，与web交互采用msgpack（压缩的json）