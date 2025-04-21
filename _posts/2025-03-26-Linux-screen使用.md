1. screen使用

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