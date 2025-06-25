1. tcpdump使用，不支持抓取加密后的https
```
# 1. 嗅探所有接口，80 端口上所有 HTTP 协议请求与响应的 headers 以及 body
tcpdump -A -s 0 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'
## 改抓 8080 端口
tcpdump -A -s 0 'tcp port 8080 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'

# 2. 嗅探 eth0 接口，80 端口上所有 HTTP GET 请求（'GET ' => 0x47455420）
tcpdump -A -i eth0 -s 0 'tcp port 80 and tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420'
## 改抓 8080 端口
tcpdump -A -i eth0 -s 0 'tcp port 8080 and tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420'

# 3. 嗅探 eth0 接口，80 端口上所有 HTTP POST 请求（'POST' => 0x504F5354）
tcpdump -A -i eth0 -s 0 'tcp port 80 and tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504F5354'
## 改抓 8080 端口
tcpdump -A -i eth0 -s 0 'tcp port 8080 and tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504F5354'

# 4. 也可以使用 not 进行参数排除，比如排除掉 9091 跟 2379 端口
tcpdump -A -s 0 'tcp and port not 9091 and port not 2379 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'

# 5. 嗅探 eth0 接口， src/dst ip 地址为 x.x.x.x/a.a.a.a 的所有 tcp 数据包
tcpdump -A -i eth0 -s 0 'tcp and (host x.x.x.x or host a.a.a.a)'
# 6. 通过 ip + port 组合过滤 tcp 数据包
tcpdump -A -i eth0 -s 0  'tcp and !(dst host 192.168.1.100 and dst port 1111) and !(dst host 192.168.1.101 and dst port 3333)'
# 7. 根据 CIDR 网段过滤 tcp 数据包
tcpdump -A -i eth0 -s 0 'tcp and net 172.16.0.0/16'
```