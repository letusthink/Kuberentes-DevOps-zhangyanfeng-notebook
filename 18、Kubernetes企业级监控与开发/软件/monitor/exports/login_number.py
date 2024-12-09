from prometheus_client import start_http_server, Gauge
import subprocess
import time

# 创建一个Gauge指标，用于记录系统登录用户数量
logged_in_users = Gauge('logged_in_users', 'Number of Logged In Users')

def collect_logged_in_users():
    # 在shell中执行命令获取登录用户数量
    output = subprocess.check_output("who | wc -l", shell=True)

    # 将登录用户数量设置到logged_in_users指标中
    logged_in_users.set(int(output))

if __name__ == "__main__":
    start_http_server(8000)

    # 每隔5秒钟采集一次用户登录数量
    while True:
        time.sleep(5)
        collect_logged_in_users()
