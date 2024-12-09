from prometheus_client import start_http_server, Gauge
from kubernetes import client, config
import time

# 创建pv状态指标
pod_status = Gauge('pod_status', 'Pod Status', ['name', 'namespace', 'status'])

# 采集pod状态
def collect_pod_metrics():
    # 从kubernetes集群获取pod列表
    pod_list = client.CoreV1Api().list_pod_for_all_namespaces().items

    for pod in pod_list:
        # 获取pod的名称、命名空间和状态
        name = pod.metadata.name
        namespace = pod.metadata.namespace
        status = pod.status.phase

        # 更新pv状态指标
        pod_status.labels(name=name, namespace=namespace, status=status).set(1)

if __name__ == '__main__':
    # 加载kubernetes配置
    config.load_kube_config()

    # 启动http服务器
    start_http_server(8000)

    # 每隔5秒钟采集一次
    while True:
        collect_pod_metrics()
        time.sleep(60)
