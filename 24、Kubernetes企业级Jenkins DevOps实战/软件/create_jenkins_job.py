import jenkins
import time

# 创建 Jenkins 实例
jenkins_server = jenkins.Jenkins('http://192.168.128.11:30002', username='admin', password='admin')

def build_job(name):
    # 开始进行任务构建，等待10秒钟
    print('开始进行任务构建，请稍等！')
    jenkins_server.build_job(name)
    time.sleep(10)

    # 获取最新的构建号
    last_build_number = jenkins_server.get_job_info(name)['lastBuild']['number']
    print('本次构建号码为: ', last_build_number)

    while True:
        # 获取构建状态
        build_info = jenkins_server.get_build_info(name, last_build_number)
        build_status = build_info['result']
        # 判断任务状态是否为SUCCESS，如果为SUCCESS则说明任务构建成功。
        if build_status == "SUCCESS":
            print("构建成功！")
            break

if __name__ == "__main__":
    build_job(name='Deliver Java Project')