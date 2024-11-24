import random
class RandomizedSet:

    # Solution 1 - using list and hashmap
    # Time - O(1)
    # Space - O(n)

    def __init__(self):
        # self.random = {}
        # self.random_list = []


        # Re-do for the interview

        self.random_list = []
        self.random_index = {}

    def insert(self, val: int) -> bool:

        # if val not in self.random:
        #     self.random[val] = len(self.random_list)
        #     self.random_list.append(val)
        #     return True

        # return False

        # Re-do for the interview

        if val not in self.random_index:
            self.random_index[val] = len(self.random_list)
            self.random_list.append(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        # if val in self.random:
        #     idx = self.random[val]
        #     last_val = self.random_list[-1]
        #     self.random_list[idx] = last_val
        #     self.random_list.pop()

        #     # NOTE: This ordering is very important
        #     # Reason: if both val and last_val can be same
        #     # In this case you'll be adding it again after deleting and this will be wrong 
        #     self.random[last_val] = idx
        #     del self.random[val]

        #     return True
        # else:
        #     return False

        if val in self.random_index:
            idx = self.random_index[val]
            last_val = self.random_list[-1]
            self.random_list[idx] = last_val
            self.random_list.pop()

            self.random_index[last_val] = idx
            del self.random_index[val]

            return True
        else:
            return False


    def getRandom(self) -> int:
        # return random.choice(self.random_list) # Works by calculating index, so this function needs a list; Cannot use a set

        import random
        return random.choice(self.random_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
