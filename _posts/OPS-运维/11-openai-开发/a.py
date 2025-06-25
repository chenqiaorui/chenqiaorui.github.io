import os
import openai
import re

# optional; defaults to `os.environ['OPENAI_API_KEY']`
openai.api_key = ""

# all client options can be configured just like the `OpenAI` instantiation counterpart
openai.base_url = "https://free.v36.cm/v1/"
openai.default_headers = {"x-foo": "true"}
# 定义运维知识点数组
#knowledge_points = ['容器技术', 'df', 'tail']
knowledge_points = ['top', 'docker', 'iptables']
knowledge_points_1 = ['容器技术', 'Kubernetes', 'Docker', '微服务架构', 'CI/CD', '负载均衡', '监控与告警', '服务网格']
knowledge_points_2 = ['虚拟化技术', 'VMware', 'Hyper-V', 'OpenStack', '网络安全', '防火墙', '入侵检测', '备份与恢复']
knowledge_points_3 = ['数据库管理', 'MySQL', 'PostgreSQL', 'MongoDB', 'SQL优化', '数据迁移', '数据备份', '事务管理']
knowledge_points_4 = ['网络协议', 'TCP/IP', 'HTTP', 'HTTPS', 'DNS', 'FTP', 'SSH', 'VPN']
knowledge_points_5 = ['操作系统', 'Linux', 'Windows Server', 'Unix', 'Shell脚本', '系统监控', '资源管理', '性能调优']
knowledge_points_6 = ['配置管理', 'Ansible', 'Puppet', 'Chef', 'SaltStack', 'Terraform', '版本控制', 'Git']
knowledge_points_7 = ['日志管理', 'ELK栈', 'Fluentd', 'Graylog', 'Syslog', '日志分析', '集中式日志', '监控平台']
knowledge_points_8 = ['云计算', 'AWS', 'Azure', 'Google Cloud', '云存储', '无服务器架构', '边缘计算', '容器编排']
knowledge_points_9 = ['DevOps文化', '敏捷开发', '持续集成', '持续交付', '跨团队协作', '自动化测试', '质量保障', '反馈循环']
knowledge_points_10 = ['故障排除', '故障转移', '高可用性', '灾难恢复', '性能监控', '容量规划', '服务级别协议', '问题管理']

# 遍历每个知识点
for point in knowledge_points_2:
    # 构建请求的文本
    #prompt = f"请解释一下有关'{point}'的内容，包括它的原理、使用场景和最佳实践。"
    prompt = f"生成一个运维知识点案例，和'{point}'的内容有关。按照以下格式输出：1. 按照步骤说明要执行的操作；2. 说明必选的执行步骤；3. 说明适用的操作系统（如Centos7、Ubuntu22.04）。按照示例给出：1. 前提：操作系统：Centos7、原理、常用命令、最佳实践示范，给出的命令必须确保是真实有效。你的回答要表现得像个人类教授知识一样"
    
    # 调用OpenAI API
    completion = openai.chat.completions.create(
        #model="gpt-3.5-turbo",  # 选择适当的模型
        model="gpt-4o-mini",  # 选择适当的模型
        
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    # 获取模型的回答
    content = completion.choices[0].message.content
    # 定义Markdown文件名（使用知识点名称并替换空格为下划线）
    #md_filename = f"{point}.md".replace(" ", "_")  # 替换空格为下划线以确保文件名有效
    filename = f"{point}.md"
    md_filename = re.sub(r'[\\/:*?"<>|]', '_', filename)
    
    # 写入Markdown文件
    with open(md_filename, 'w', encoding='utf-8') as md_file:
        md_file.write(f"# {point}\n\n")
        md_file.write(content + "\n\n")