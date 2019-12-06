f = open('input.txt').readlines()

class Vertex:
    nodes = {}

    @classmethod
    def get_path(cls, name):
        node = cls.nodes[name].get_parent()
        l = []
        while node is not None:
            l.append(node._name)
            node = node.get_parent()
        return l

    @classmethod
    def get_total_depth(cls):
        total_depth = 0
        for name in cls.nodes:
            total_depth += cls.nodes[name].get_depth()
        return total_depth

    @classmethod
    def add_vertex(cls, name, parent_name=None):
        v_parent=None
        if parent_name is not None:
            if parent_name in cls.nodes:
                v_parent = cls.nodes[parent_name]
            else:
                v_parent = Vertex(parent_name, parent=None)
                cls.nodes[parent_name] = v_parent
        node = None
        if name in cls.nodes:
            node = cls.nodes[name]
            if v_parent is not None:
                node.set_parent(v_parent)
        else:
            node = Vertex(name, v_parent)
            cls.nodes[name] = node


        
    def __init__(self, name, parent=None):
        self._parent = parent
        self._name = name

    def set_parent(self, parent):
        self._parent = parent

    def get_parent(self):
        return self._parent

    def get_depth(self):
        if self._parent is None:
            return 0
        else:
            return self._parent.get_depth()+1



for a in f:
    nodes = a.strip().split(')')
    parent_name = nodes[0]
    child_name = nodes[1]
    Vertex.add_vertex(child_name, parent_name=parent_name)

print(Vertex.get_total_depth())
#part2
l_you = Vertex.get_path('YOU')[::-1]
l_san = Vertex.get_path('SAN')[::-1]


for i in range(len(l_you)):
    if l_you[i]!=l_san[i]:
        break

print('Min steps {}'.format(len(l_you) - i + len(l_san) - i))







    
