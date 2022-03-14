import queue
import time
from Node import * 

priorityQueue = queue.PriorityQueue()
nodes = Node.init_simplified_yogyakarta()

start = nodes['Bandarlampung']
goal = nodes['Yogyakarta']

visited = {}

for node in nodes:
    visited[node] = False

start_time = time.perf_counter_ns()
priorityQueue.put((start.get_heuristic_value(), start))
total_distance = 0
node = start

while not priorityQueue.empty():
    last_node = node
    node = priorityQueue.get()[1]

    if node != start:
        total_distance += last_node.child[node]['w']
        last_node = node

    visited[node] = True
    print(f'{node.name} ---> ', end='')
    if node == goal:
        print("END")
        break
    for child in node.child:
        if child not in visited:
            priorityQueue.put((child.get_heuristic_value(), child))

print("Total Jarak\t %s" % total_distance)
print("Waktu Eksekusi\t %s ns" % (time.perf_counter_ns() - start_time))