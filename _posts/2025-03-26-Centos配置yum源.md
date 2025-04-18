### 1. 配置 yum 源并安装
```
wget http://mirrors.163.com/.help/CentOS7-Base-163.repo		#下载网络yum源
mv CentOS7-Base-163.repo /etc/yum.repos.d/			#移动到yum源下
yum clean all							#清空缓存
yum makecache							#建立其库
yum -y install mariadb mariadb-server httpd php php-mysql
```
