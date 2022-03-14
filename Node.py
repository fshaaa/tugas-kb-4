class Node:
    def __init__(self, name, heuristic_val=0):
        # child adalah dict of node, yang mapping jarak current node ke child, state adalah state node 
        # parent itu node di atas sekarang
        self.name            = name
        self.__heuristic_val = heuristic_val
        self.child           = {}

    def add_or_update_child(self, child):
        self.child.update(child)

    def set_heuristic_value(self, value):
        self.__heuristic_val = value

    def get_heuristic_value(self):
        return self.__heuristic_val

    def remove_child(self, child):
        del self.child[child]

    @staticmethod
    def init_simplified_yogyakarta():
        # nilai heuristic yang dimasukkan di sini adalah straight line distance
        # ke bucharest
        nodes = {
            'Bandarlampung' : Node('Bandarlampung', 629),
            'Jakarta'       : Node('Jakarta', 446),
            'Bogor'         : Node('Bogor', 421),
            'Bandung'       : Node('Bandung', 320),
            'Cirebon'       : Node('Cirebon', 246),
            'Tasikmalaya'   : Node('Tasikmalaya', 248),
            'Purwokerto'    : Node('Purwokerto', 132),
            'Cilacap'       : Node('Cilacap', 156),
            'Semarang'      : Node('Semarang', 108),
            'Yogyakarta'    : Node('Yogyakarta', 0),
        }

        nodes['Bandarlampung'].add_or_update_child({
            nodes['Jakarta']: {
                'w': 233
            },
        })
        nodes['Jakarta'].add_or_update_child({
            nodes['Bandarlampung']: {
                'w': 233
            },
            nodes['Bogor']: {
                'w': 56
            },
            nodes['Cirebon']: {
                'w': 219
            },
        })
        nodes['Bogor'].add_or_update_child({
            nodes['Jakarta']: {
                'w': 56
            },
            nodes['Bandung']: {
                'w': 124
            },
        })
        nodes['Bandung'].add_or_update_child({
            nodes['Bogor']: {
                'w': 124
            },
            nodes['Cirebon']: {
                'w': 129
            },
            nodes['Tasikmalaya']: {
                'w': 111
            },
        })
        nodes['Cirebon'].add_or_update_child({
            nodes['Jakarta']: {
                'w': 219
            },
            nodes['Bandung']: {
                'w': 129
            },
            nodes['Cilacap']: {
                'w': 170
            },
            nodes['Purwokerto']: {
                'w': 146
            },
            nodes['Semarang']: {
                'w': 234
            },
        })
        nodes['Tasikmalaya'].add_or_update_child({
            nodes['Bandung']: {
                'w': 111
            },
            nodes['Cilacap']: {
                'w': 140
            },
        })
        nodes['Purwokerto'].add_or_update_child({
            nodes['Cirebon']: {
                'w': 146
            },
            nodes['Cilacap']: {
                'w': 50
            },
            nodes['Yogyakarta']: {
                'w': 168
            },
        })
        nodes['Cilacap'].add_or_update_child({
            nodes['Tasikmalaya']: {
                'w': 140
            },
            nodes['Cirebon']: {
                'w': 170
            },
            nodes['Purwokerto']: {
                'w': 50
            },
            nodes['Yogyakarta']: {
                'w': 172
            },
        })
        nodes['Semarang'].add_or_update_child({
            nodes['Cirebon']: {
                'w': 234
            },
            nodes['Yogyakarta']: {
                'w': 130
            },
        })
        nodes['Yogyakarta'].add_or_update_child({
            nodes['Purwokerto']: {
                'w': 168
            },
            nodes['Cilacap']: {
                'w': 172
            },
            nodes['Semarang']: {
                'w': 130
            },
        })

        return nodes
