1. ulimit -n 单个进程可以同时打开的文件描述符的最大值，缺省1024
2. Hard和Soft，Hard是Soft的最高限值，天花板。

临时生效：
`ulimit -S -n 10240  `

`ulimit -H -n 20480`

永久生效：

vi /etc/security/limits.conf

```
* soft nofile 65536
* hard nofile 65536
* soft nproc 131072
* hard nproc 131072
```