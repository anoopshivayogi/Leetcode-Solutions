class MyHashSet:

    def __init__(self):
        # self.set = [False] * (10**6 + 1)

        # Solution 1 - Using linkedlist as buckets
        # Time - 
        # Space - 

        self.key_range = 700
        self.bucket_arr = [Bucket() for _ in range(self.key_range)] 

        
    def add(self, key: int) -> None:
        # self.set[key] = True

        # Solution 1
        self.bucket_arr[key % self.key_range].insert(key)

    def remove(self, key: int) -> None:
        # self.set[key] = False

        # Solution 1
        self.bucket_arr[key % self.key_range].delete(key)
        
    def contains(self, key: int) -> bool:
        # return self.set[key]

        # Solution 1
        return self.bucket_arr[key % self.key_range].exists(key)


class Node:
    def __init__(self, val=-1, nxt=None):
        self.val = val
        self.nxt = None

class Bucket:

    def __init__(self):
        self.head = Node() # Pseudo Head with val=-1

    def insert(self, key):
        if not self.exists(key):  # NOTE: insert only if the key already doesn't exist in this bucket.
            cur = self.head

            while cur.nxt:
                cur = cur.nxt

            cur.nxt = Node(val=key)
        
    def delete(self, key):
        prev = self.head
        cur = prev.nxt

        while cur:
            if cur.val == key:
                prev.nxt = cur.nxt
                return
            prev = cur
            cur = cur.nxt
        
    def exists(self, key):
        cur = self.head.nxt

        while cur:
            if cur.val == key:
                return True
            cur = cur.nxt

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)