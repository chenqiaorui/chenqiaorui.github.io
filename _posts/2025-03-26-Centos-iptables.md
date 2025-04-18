### 1. iptables 安装使用
```
yum install -y iptabels-services -y
systemctl enable iptables.service
vi /etc/sysconfig/iptables
systemctl restart iptables
```
