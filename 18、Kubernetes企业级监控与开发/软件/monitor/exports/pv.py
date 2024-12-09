from prometheus_client import start_http_server, Gauge
from kubernetes import client, config
import time

# 创建pv状态指标
pv_status = Gauge('pv_status', 'PV Status', ['name', 'phase', 'access_mode', 'capacity', 'storage_class_name'])

# 采集pv状态
def collect_pv_metrics():
    # 从kubernetes集群获取pv列表
    pv_list = client.CoreV1Api().list_persistent_volume().items

    for pv in pv_list:
        # 获取pv的名称、状态、访问模式、容量、供应商
        name = pv.metadata.name
        phase = pv.status.phase
        access_modes = ', '.join(pv.spec.access_modes)
        capacity = pv.spec.capacity.get('storage', '')
        storage_class_name = pv.spec.storage_class_name

        # 更新pv状态指标
        pv_status.labels(name=name, phase=phase, access_mode=access_modes, capacity=capacity, storage_class_name=storage_class_name).set(1)

if __name__ == '__main__':
    # 加载kubernetes配置
    config.load_kube_config()

    # 启动http服务器
    start_http_server(8000)

    # 每隔5秒钟采集一次
    while True:
        collect_pv_metrics()
        time.sleep(60)
