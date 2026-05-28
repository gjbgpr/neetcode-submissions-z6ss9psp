class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        node = self.hmap[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            old_node = self.hmap[key]
            self.remove(old_node)
        
        node = ListNode(key, value)
        self.add(node)
        self.hmap[key] = node
        
        if len(self.hmap) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.hmap[node_to_delete.key]

        
    def remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add(self, node: ListNode) -> None:
        curr = self.tail.prev
        self.tail.prev = node
        curr.next = node
        node.prev = curr
        node.next = self.tail