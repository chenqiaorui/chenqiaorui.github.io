hostnamectl set-hostname <newName>  # 修改主机名，重启生效


## screen背景
系统管理员经常需要SSH 远程登录到Linux 服务器，经常运行一些需要很长时间才能完成的任务，比如系统备份、ftp 传输等等。
通常情况下我们都是为每一个这样的任务开一个远程终端窗口，因为它们执行的时间太长了。必须等待它们执行完毕，在此期间不能关掉窗口或者断开连接，否则这个任务就会被杀掉，一切半途而废了。

screen可以解决上述问题，screen在其内部运行的会话都可以恢复。这一点对于远程登录的用户特别有用——即使网络连接中断，用户也不会失去对已经打开的命令行会话的控制。只要再次登录到主机上执行 screen -r就可以恢复会话的运行。

实战：
1. yum install screen
2. screen -S test1 # 新建并进入screen窗口

touch test.sh, 文件内容：

while true
do
  echo "输出`date +%F-%T`"
  sleep 10
done

3. 执行：sh test.sh
4. 新开一个会话窗口，使test1窗口离线
  screen -d test1
5. 重连窗口：screen -r test1, 发现test.sh脚本一直在执行

其他：在test1窗口内执行exit，退出并杀死screen窗口。

==============================================================================

1. screen其他使用

通过执行 screen 来新建一个会话，使用 Ctrl + A,D 离开该会话，会话将在后台继续运行，之后 screen -ls 可以查看会话列表。 使用 screen -r pid或tty或host 恢复会话，使用 exit 可以退出会话，会话不会再运行。

```
yum install screen  
screen -S yourname # 新建一个叫 yourname 的 session
screen -ls # 列出当前所有的 session
screen -r yourname # 回到 yourname 这个 session
screen -d yourname # 远程 detach 某个 session
screen -d -r yourname # 结束当前 session 并回到 yourname 这个session
```

https://199604.com/1478