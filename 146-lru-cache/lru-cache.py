class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(key)
            self.insert(key, node.val)
            return(node.val)
        return -1

    def put(self, key: int, val: int) -> None:
        if key in self.map:
            self.remove(key)
            self.insert(key, val)
            return
        
        if self.capacity == len(self.map):
            self.remove(-1)
        self.insert(key,val)
        return
    
    def remove(self, key):
        if key==-1:
            del self.map[self.left.next.key]
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
        else:
            node = self.map[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.map[key]
        return


    def insert(self, key, val):
        self.map[key] = Node(key,val)

        temp = self.right.prev
        self.right.prev = self.map[key]
        self.map[key].next = self.right

        self.map[key].prev = temp
        temp.next = self.map[key]
        return
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)