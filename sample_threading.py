import threading
import time

def worker():
    print(f'{threading.current_thread().name} is working')
    time.sleep(1)
    print(f'{threading.current_thread().name} is done')

for _ in range(5):
    # 创建线程
    t = threading.Thread(target=worker)
    # 给每个线程起一个名字
    t.name = 'Thread-' + str(_)
    t.start()