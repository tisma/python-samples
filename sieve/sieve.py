class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.prev = None
        self.next = None


class SieveCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None
        self.hand = None
        self.size = 0

    def _add_to_head(self, node):
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node

    def _remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def _evict(self):
        obj = self.hand if self.hand else self.tail
        while obj and obj.visited:
            obj.visited = False
            obj = obj.prev if obj.prev else self.tail
        self.hand = obj.prev if obj.prev else None
        del self.cache[obj.value]
        self._remove_node(obj)
        self.size -= 1

    def access(self, x):
        if x in self.cache:
            node = self.cache[x]
            node.visited = True
        else:
            if self.size == self.capacity:
                self._evict()
            new_node = Node(x)
            self._add_to_head(new_node)
            self.cache[x] = new_node
            self.size += 1
            new_node.visited = False

    def show_cache(self):
        current = self.head
        while current:
            print(f'{current.value} (Visited: {current.visited})', end=' -> ' if current.next else '\n')
            current = current.next

cache = SieveCache(3)
cache.access('A')
cache.access('B')
cache.access('C')
cache.access('D')
cache.show_cache()

