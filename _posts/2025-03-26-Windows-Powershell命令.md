### 1. Powershell 命令
```
Clear-DnsClientCache  # 清除 dns 缓存（替换掉 `ipconfig /flushdns`）
Get-DnsClientCache  # 查看 dns 缓存
Resolve-DnsName baidu.com  # 解析域名

tasklist /svc | findstr TermService # 查看远程桌面端口
netstat -ano|findstr 1200
```
