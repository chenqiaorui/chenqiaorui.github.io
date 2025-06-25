```
mkdir -p /etc/docker

sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["xxx"]
}
EOF

sudo systemctl daemon-reload
sudo systemctl restart docker
```

#### 国内拉docker镜像有问题，需设置代理
```
vi /lib/systemd/system/docker.service

在[Service]块ExecStart行前添加如下文本：
Environment="HTTP_PROXY=http://215.215.0.2:10809"
Environment="HTTPS_PROXY=http://215.215.0.2:10809"

systemctl daemon-reload
systemctl restart docker

# 验证
systemctl show --property=Environment docker
```

#### 通过docker容器查看run命令

`https://zahui.fan/posts/lt41mupw/`

#### docker-compose模板

`https://github.com/yeasy/docker-compose-files`



#### centos 安装docker
```
Q: 以下是在CentOS操作系统上安装Docker的步骤：

# 卸载旧版本的Docker（如果安装过）
sudo yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine

# 安装必要的依赖项
sudo yum install -y yum-utils device-mapper-persistent-data lvm2

# 使用以下命令设置稳定版Docker的存储库
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# 更新yum软件包索引，然后安装最新版本的Docker Engine和containerd
sudo yum update -y
sudo yum install -y docker-ce docker-ce-cli containerd.io

# 启动Docker服务并将其设置为开机启动
sudo systemctl start docker
sudo systemctl enable docker
#验证Docker是否已正确安装
sudo docker run hello-world 

如果一切正常，您应该会看到一条消息，指示Docker正在运行，并向您发送问候。
```