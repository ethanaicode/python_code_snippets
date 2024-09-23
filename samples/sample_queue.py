import queue

# 创建一个队列
q = queue.PriorityQueue()

# 向队列中添加元素
q.put((1, 'A'))

# 从队列中取出元素
_, item = q.get()

print(item)