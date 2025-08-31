
# Solution 1 - Brute force, creating hashmap using same size array
# Time - O(1)
# Space - O(10^5)

# class MyHashMap:

#     def __init__(self):
#         self.map = [-1] * 10000000        

#     def put(self, key: int, value: int) -> None:
#         self.map[key] = value
        

#     def get(self, key: int) -> int:
#         return self.map[key]

#     def remove(self, key: int) -> None:
#         self.map[key] = -1


# Solution 2 - Array of size 10000 with linkedlist
# Time - O(1) Average time complexity is at O(1)
# Space - O(1000) -> Constant 
# NOTE - You can grow the size of the array as the number of elements increases, This is what is done in real world

class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.data = [ListNode() for i in range(1000)]
        

    def getHash(self, key):
        return key % len(self.data)


    def put(self, key: int, value: int) -> None:
        cur = self.data[self.getHash(key)]

        while cur.next:  # Check if it already exists and update it if it does.
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next

        cur.next = ListNode(key=key, val=value)


    def get(self, key: int) -> int:
        cur = self.data[self.getHash(key)]

        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next

        return -1


    def remove(self, key: int) -> None:
        cur = self.data[self.getHash(key)]

        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                break

            cur = cur.next
    


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)