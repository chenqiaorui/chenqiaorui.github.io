`traceroute -n -T -p 443 192.168.1.10`

- -T 使用tcp
- -p 端口

- 淘宝IP地址库：ip.taobao.com/ipSearch

#### 探测案例

** 探测结果：探测结果如下，目标端口在第11跳之后就没有数据返回，说明相应端口在该节点被阻断。**
```
[root@mycentos ~]# traceroute -T -p 135 www.baidu.com
traceroute to www.baidu.com (111.13.XXX.XXX), 30 hops max, 60 byte packets
 1  * * *
 2  111.13.XXX.XXX (111.13.XXX.XXX)  4.115 ms  4.397 ms  4.679 ms
 3  112.15.XXX.XXX (112.15.XXX.XXX)  901.921 ms  902.762 ms  902.338 ms
 4  200.35.XXX.XXX (200.35.XXX.XXX)  2.187 ms  1.392 ms  2.266 ms
 5  * * *
 6  58.200.XXX.XXX (58.200X.XXX.XXX)  1.688 ms  1.465 ms  1.475 ms
 7  63.128.XXX.XXX (63.128.XXX.XXX)  27.729 ms  27.708 ms  27.636 ms
 8  * * *
 9  * * *
10  200.38.XXX.XXX (200.38.XXX.XXX)  28.922 ms 200.38.XXX.XXX (200.38.XXX.XXX)   29.030 ms  28.916 ms
11  204.35.XXX.XXX (204.35.XXX.XXX)  29.169 ms  28.893 ms 204.35.XXX.XXX (204.35.XXX.XXX)  30.986 ms
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
```

https://www.alibabacloud.com/help/zh/ecs/user-guide/troubleshoot-the-issue-that-an-instance-can-be-pinged-but-the-required-port-cannot?spm=a2c63.p38356.help-menu-25365.d_4_5_10_1.661e2305w9mQfo