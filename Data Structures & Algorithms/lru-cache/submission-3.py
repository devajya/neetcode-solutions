class LRUCache:
    class Node:
        def __init__(self, key=-1, value=-1):
            self.k = key
            self.v = value
            self.next_node = None
            self.prev_node = None
        
    def __init__(self, capacity: int):
        self.cap = capacity
        self.maps = {}
        self.head = self.Node()
        self.tail = self.Node()

        self.head.next_node = self.tail
        self.tail.prev_node = self.head

    def remove(self, node: Node) -> None:
        prv = node.prev_node
        nxt = node.next_node
        prv.next_node = nxt
        nxt.prev_node = prv

    def add_to_top(self, node: Node) -> None:
        end = self.head.next_node
        self.head.next_node = node
        node.prev_node = self.head
        node.next_node = end
        end.prev_node = node

    def get(self, key: int) -> int:
        if key not in self.maps:
            return -1
        
        n = self.maps[key]
        self.remove(n)
        self.add_to_top(n)
        return n.v
        
    def put(self, key: int, value: int) -> None:
        if key in self.maps:
            n = self.maps[key]
            self.remove(n)
            n.v = value
            self.add_to_top(n)
        else:
            if len(self.maps) >= self.cap:
                n = self.tail.prev_node
                self.remove(n)
                del self.maps[n.k]
             
            n = self.Node(key, value)
            self.maps[key] = n
            self.add_to_top(n)
    
