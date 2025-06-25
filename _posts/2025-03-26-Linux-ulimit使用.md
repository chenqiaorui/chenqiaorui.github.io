#### 注解
- 1. ulimit -n 单个进程可以同时打开的文件描述符的最大值，缺省1024
- 2. Hard和Soft，Hard是Soft的最高限值，天花板。
- 3. 已用文件描述符数量，lsof | wc -l


#### 永久生效：

vi /etc/security/limits.conf

```
* soft nofile 65535
* hard nofile 65535
* soft nproc 131072
* hard nproc 131072
```

接着，调整系统打开文件数量限制，编辑 /etc/sysctl.conf，
fs.file-max= 65535

执行 `sysctl -p` 立即生效。

编辑 /etc/profile：`ulimit -SHn 65535`