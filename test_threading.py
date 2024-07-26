import threading
import time

def worker():
    print(threading.current_thread().name, ' mid')
    print(f'{threading.current_thread().name} is working')
    time.sleep(1)
    print(f'{threading.current_thread().name} is done')

for _ in range(5):
    # 创建线程
    print(threading.current_thread().name, ' start')
    t = threading.Thread(target=worker, name='Thread-' + str(_))
    print(threading.current_thread().name, ' end')
    t.start()