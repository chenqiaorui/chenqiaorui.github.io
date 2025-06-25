##### 数字比较符eq
```
只能比较数字，若字符则会被转成数字，如字符0不会等于数字0

-ne // 不等于
-gt // 大于
-eq // 等于
-lt // 小于

if [ 1 -eq 0 ];then
	echo "eq"
fi
```

##### 特殊变量
```
$0 当前脚本名称
$n 传递给脚本的第几个参数，如$1获取第一个参数
$# 传递给脚本的参数个数
$* 传递给脚本的所有参数
$? 上个命令的退出状态
$$ 当前shell的pid

# 示例
cd /optsafjlajdk
echo $?  // 切换到一个不存在的目录，返回1不正常状态
```

##### if/else
```
branch_name="test"

if [ ${branch_name} == "test" ];then
	echo "yes"
else
	echo "no"
fi
```

##### case
```
env=$1
case $env in
  release)
	echo "release"
	wait
	;;
  test)
	echo "test"
	wait
	;;
  *)
	echo "any"
	;;
esac;
```

##### 文件表达式
```
// -e 文件存在则为真
// -d 目录存在则为真
// -s 判断文件是否为空

if [ -s empty.log ];then
	echo "not emp"
else
	echo "emp"
fi

if [ -d test1 ];then
	echo "存在";
fi
```

##### 字符串表达式比较
```
a="a"
b="a"
c="c"
if [ $a = $b -o $a = $c ];then
        echo "eq"
fi

// Note: $a = $b 不能写成$a=$b
// -o 表逻辑或
// -a 表逻辑与
// ! 表逻辑非，如if [ $a != $c ]
```

##### for
```
for i in `seq 10`;do
	echo $i
done
```

##### sh -x 显示执行过程
```
例子1：
如有脚本test.sh，内容:

echo "hello"

执行sh -x test.sh，结果：

+ echo hell
hell
```
```
例子2：
echo "hell"

echo `dirname $PWD`  # 注意这条语句包含多个执行过程，打印结果的时候会有两个+号

执行后，
+ echo hell
hell
++ dirname /opt/test/process
+ echo /opt/test
/opt/test
```

```sh -n``` 
检查脚本语法

```time sh test.sh``` 
脚本执行时间

##### set
set -e      # 若指令传回值不为0，立即退出脚本

### linux常用命令
```
zip -qr yasuo.zip yasuo # -q变不显示压缩信息，-r 表递归压缩下面层级的目录或文件

cat access.log| awk '{print $4}'|sort | uniq -c| sort -nr # 排序

# 查找1天前以.gz结尾的日志，并批量删除
find /var/log/nginx/ -name "*.gz" -type f -mtime +1|xargs rm -f

## vim技巧
:set ff # 查看文本格式
:set binary # 改为unix格式
```


#### 常用示例
crontab -e 打开配置文件
-l # 显示当前用户的定时任务内容
-r # 删除用户/var/spool/cron/ 定时任务
```
*/1 * * * * /usr/sbin/chroot --userspec=nobody.nobody / sh -c "echo 'nobody' > /tmp/nobody.log "
```

### cron表达式验证
```
https://www.iamwawa.cn/crontab.html
```

#### 例子：grep
```
grep "ricky" test.log   # 只取选中的字符所在行
grep -v "ricky" test.log  # 取不选中的行
grep -r "ricky" ./*   # 递归查找当前目录及子目录下的ricky
grep -e "rick*" test.log  # 开启正则匹配模式
grep -w 'ricky' txt                          # 精确匹配字符串，-w只会匹配单独存在的ricky，如文本里存在arickya不会被匹配到，但a ricky a 会
```
#### SSH-远程连接工具
```
ssh root@192.168.1.2 -p 22
ssh-keygen # 生成`id_rsa.pub`和 `id_rsa.private`
/etc/ssh/sshd_config # 配置文件入口，可以修改端口等
systemctl status sshd # 服务管理
```


##### 什么是平均负载
看一个例子：`uptime`
```
$ uptime
02:34:03 up 2 days, 20:14,  1 user,  load average: 0.63, 0.83, 0.88
```
说明：
- `02:34:03` 当前时间
- `up 2 days, 20:14` 系统从开机后运行的时长
- `1 user` 正在登录的用户数
- `load average: 0.63, 0.83, 0.88` 最近1分钟、5分钟、15分钟的平均负载(Load average)

`平均负载`是指单位时间内，系统处于可运行(Running或ready)和不可中断(blocked)的进程数。结合最近1分钟、5分钟、15分钟的平均负载，我们可以全面了解cpu的使用情况。像了解一天早中晚的气候变化。

Running是指正在使用cpu；Ready是指代码(指令)已经加载到了内存，等cpu来执行指令；

不可中断是指进程在使用cpu，突然需要进行磁盘IO(读写)的长时间操作，先不用cpu，等IO操作完毕再回来使用cpu。

一般而言，平均负载超过cpu核数70%就要检查cpu的使用情况，考虑是否优化。

查看cpu核数
```
grep 'model name' /proc/cpuinfo|wc -l
```

##### 什么是CPU使用率
cpu使用率衡量了单位时间cpu的繁忙程度。

对于I/O密集型进程，平均负载就高，但cpu却不繁忙，也就是cpu使用率不高。

看一个例子：`top`
```
$ top
top - 11:15:27 up 40 days, 51 min,  1 user,  load average: 0.32, 0.27, 0.26
Tasks: 356 total,   1 running, 355 sleeping,   0 stopped,   0 zombie
%Cpu(s):  4.2 us,  5.6 sy,  0.0 ni, 90.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   7777.8 total,    281.6 free,   4394.8 used,   3101.3 buff/cache
MiB Swap:   2048.0 total,    580.2 free,   1467.8 used.   3015.1 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                                                                 
3811294 root      20   0   15440   4540   3768 R  20.0   0.1   0:00.03 top                                                                                                                     
    682 avahi     20   0   10524   5696   3120 S   6.7   0.1 110:29.16 avahi-daemon                                                                                                            
   7726 root      20   0  750872  21192   5772 S   6.7   0.3 259:56.50 travel-api  
```
说明：
- `%Cpu(s)` 比如说有4个cpu，%Cpu(s)代表这4个的平均使用率。

  cpu = 用户空间使用率(us) + 内核空间使用率(sy) + 空闲(id)

  `ni` 用户空间通过改变进程优先级占用的cpu百分比

  `wa` 等待io操作占用的cpu百分比

  `hi/si` 硬/软中断进行cpu上下文切换占用的百分比

- `RES` 使用的真实物理内存（KB）
- `%CPU` 一个cpu的使用率，毕竟一个进程只占用一个cpu
- `TIME+` 累计使用cpu时间

附top使用快捷键说明：
- `shift + m` # 按照内存使用率排序，shift m 等价于大写M
- `shift + p` # 按照cpu使用率排序
- `c` # 显示命令全路径
- `F` # 挑选你要选择展示的列，按下空格选中，* 代表会展示的列(列会出现在最后)，按q退出。
    可以展示进程使用哪一个cpu
- 按`1` # 展示每个cpu的使用情况