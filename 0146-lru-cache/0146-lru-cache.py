# class Node:
#     def __init__(self, key = 0, val=0, next=None, prev=None) -> None:
#         self.val = val
#         self.key = key
#         self.next = next
#         self.prev = prev


# class Node:
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.next = None
#         self.prev = None


class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    # def print_ll(self, root=None):
    #     while root:
    #         print(root.val)
    #         root = root.next

    def __init__(self, capacity: int):
        # self.capacity = capacity
        # # Left - Most recently used and Right - Least recently used
        # self.left, self.right = Node(val=-1), Node(val=-2)
        # self.left.next, self.right.prev = self.right, self.left
        # self.map = {}

        # Test code
        # self.print_ll(self.left)
        # n = Node(1)
        # self.insert(n)
        # self.print_ll(self.left)
        # self.remove(n)
        # self.print_ll(self.left)

        # NEW

        self.left, self.right = Node(-1, -1), Node(-2, -2)
        self.left.next, self.right.prev = self.right, self.left
        self.capacity = capacity
        self.map = {}


    def insert(self, node):  # insert from the right
        # self.right.prev.next = node
        # node.prev = self.right.prev
        # self.right.prev = node
        # node.next = self.right

        # New  -- Insert from the right
        self.right.prev.next = node
        node.prev = self.right.prev

        node.next = self.right
        self.right.prev = node


    def remove(self, node):
        # node.prev.next = node.next
        # node.next.prev = node.prev

        # New - delete the node
        node.prev.next = node.next
        node.next.prev = node.prev



    def get(self, key: int) -> int:
        # if key in self.map:
        #     self.remove(self.map[key])
        #     self.insert(self.map[key])
        #     return self.map[key].val
        # # self.print_ll(self.left)
        # return -1

        # NEW
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val

        return -1


    def put(self, key: int, value: int) -> None:
        # if key in self.map:
        #     self.remove(self.map[key])
        #     self.insert(self.map[key])
        #     self.map[key].val = value
        # else:
        #     if self.capacity == 0:
        #         del self.map[self.left.next.key]
        #         self.remove(self.left.next)
        #         self.capacity += 1
        #     self.map[key] = Node(key, value)
        #     self.insert(self.map[key])
        #     self.capacity -= 1

        # NEW

        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            self.map[key].val = value
        else:
            if self.capacity == 0:
                del self.map[self.left.next.key]
                self.remove(self.left.next)
                self.capacity += 1
            new_node = Node(key, value)
            self.map[key] = new_node
            self.insert(new_node)
            self.capacity -= 1


    # # Remove the node from the left side -- Least Recenty used
    # def remove(self, node):
    #     # node.prev.next = node.next
    #     # node.next.prev = node.prev

    #     # NEW


    # # Insert from the right - More Frequently used
    # def insert(self, node):
    #     # self.right.prev.next = node
    #     # node.prev = self.right.prev
    #     # node.next = self.right
    #     # self.right.prev = node

    #     # NEW

    # DRY-RUN
    #    capcacity = 1
    #    left - {2: 2}- {3: 3} right
    #    mapping = {2: 2, 3: 3}

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)