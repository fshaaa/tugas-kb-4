from PQueue import *
from Node import *
import time

class AStarSearch:
    def __init__(self, node):
        self.__pqueue = PQueue()
        self.__pqueue.change_sort_key(self.__sort_by_heuristic_and_distance)
        self.__visited = None
        self.__route = None
        self.__found = False
        self.__verbose = False
        self.__node = node

    @staticmethod
    def __sort_by_heuristic_and_distance(value):
        return value['distance'] + value['node'].get_heuristic_value()

    def log(self, msg):
        if (self.__verbose): print(msg)

    def __insert_to_queue(self, node, distance, from_node=None):
        self.__pqueue.insert({
            'node': node,
            'distance': distance,
            'from': from_node
        })

    def change_node(self, node):
        self.__node = node

    def get_route(self):
        if self.__found:
            return self.__route
        return None

    def get_visited(self):
        if self.__found:
            return self.__visited
        return None

    def is_found(self):
        return self.__found

    def __extract_route(self):
        node = list(self.__visited.keys())[-1]

        if self.__route != None:
            del self.__route
        self.__route = []

        self.__route.append(node)
        while self.__visited[node]['from'] != None:
            node = self.__visited[node]['from']
            self.__route.append(node)
        self.__route.reverse()

    def search(self, target):
        self.__visited = {}
        self.__pqueue.clear()
        self.__found = False

        self.__insert_to_queue(self.__node, 99999)

        while not self.__found or self.__pqueue.length() > 0:
            popped_val = self.__pqueue.pop()

            """
            cek dulu di visited ada nggak,
                nggak ada masukkin,
                ada cek kalau distance lebih pendek,
                    kalau iya update from dan distance
            """
            if popped_val['node'] in self.__visited:
                visited = self.__visited[popped_val['node']]
                if visited['distance'] > popped_val['distance']:
                    visited['distance'] = popped_val['distance']
                    visited['from'] = popped_val['from']
            else:
                # masukkan ke visited
                self.__visited[popped_val['node']] = {
                    'from': popped_val['from'],
                    'distance': popped_val['distance']
                }

            if target == popped_val['node']:
                self.__found = True
                self.__extract_route()
                break

            for child in popped_val['node'].child:
                self.__insert_to_queue(
                    child,
                    popped_val['node'].child[child]['w'] + popped_val['distance'],
                    popped_val['node']
                )

if __name__ == '__main__':
    nodes = Node.init_simplified_yogyakarta()
    finder = AStarSearch(nodes['Bandarlampung'])

    start_time = time.perf_counter_ns()
    finder.search(nodes['Yogyakarta'])
    
    if finder.is_found():
        out = "Ketemu route dari Badarlampung ke Yogyakarta: "
        prev = None
        dist = 0
        for r in finder.get_route():
            out = out + r.name
            if prev != None:
                out = out + "(" + str(prev.child[r]['w']) + ")"
                dist = dist + prev.child[r]['w']
            prev = r
            out = out + " -> "
        out = out + "sampai"
        print(out, "jarak =", dist)

print("Waktu Eksekusi\t %s ns" % (time.perf_counter_ns() - start_time))