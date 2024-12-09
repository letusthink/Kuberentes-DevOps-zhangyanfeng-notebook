from prometheus_client import start_http_server, Gauge
import subprocess
import time

# 创建一个Gauge指标
# 剩余的空闲内存
memory_available = Gauge('memory_available', 'Memory Available')

# 总内存大小
memory_total = Gauge('memory_total', 'Memory Total')

# 使用的内存大小
memory_used = Gauge('memory_used', 'Memory Userd')

def collect_memory():
    # 获取并传递剩余内存大小
    memory_available_output = subprocess.check_output(
        "free | grep Mem | awk '{print $7}'", shell=True
    )
    memory_available.set(int(memory_available_output))

    # 获取并传递总内存大小
    memory_total_output = subprocess.check_output(
        "free | grep Mem | awk '{print $2}'", shell=True
    )
    memory_total.set(int(memory_total_output))

    # 获取并传递使用内存大小
    memory_used_output = subprocess.check_output(
        "free | grep Mem | awk '{print $3}'", shell=True
    )
    memory_used.set(int(memory_used_output))

if __name__ == "__main__":
    start_http_server(8000)

    # 每隔5秒钟采集一次
    while True:
        time.sleep(5)
        collect_memory()
