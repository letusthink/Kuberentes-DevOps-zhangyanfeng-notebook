import jenkins

# 创建Jenkins实例，jenkins地址、登录名、密码
jenkins_server = jenkins.Jenkins('http://192.168.128.11:30002', username='admin', password='admin')

def list_job():
    # 获取可用的任务列表
    job_list = jenkins_server.get_jobs()

    # 提取列表中每个字典的name键对应的值
    names = [item['name'] for item in job_list]
    for name in names:
        print(name)

if __name__ == "__main__":
    list_job()