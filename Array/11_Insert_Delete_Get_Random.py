# Question : Implement the RandomizedSet class:RandomizedSet() Initializes the RandomizedSet object.bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.int getRandom() Returns a random element from the curreset of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.You must implement the functions of the class such that each function works in average O(1) time complexity.
# Approach : I used one hashmap to track value along with its index and one list for storing values. For inserting i checked if value is present in map , if not present , i inserted that value at last position of list . For deleting element i checked if value is present in hashmap , if present , i tracked its index then copied last value of list on the position where target value is present . Then i deleted last element from list . At last i updated index of last element whch is copied to new index in hashmap.
# Time Complexity : O(1)

    def __init__(self):
        self.numsMap= {}
        self.numsList = []

        

    def insert(self, val: int) -> bool:
        result = val not in self.numsMap
        if result:
            self.numsMap[val] = len(self.numsList)
            self.numsList.append(val)
        return result
        

    def remove(self, val: int) -> bool:
        result = val in self.numsMap
        if result:
            index = self.numsMap[val]
            lastValue = self.numsList[-1]
            self.numsList[index] = lastValue
            self.numsList.pop()
            self.numsMap[lastValue]= index
            del self.numsMap[val]
        return result
        

    def getRandom(self) -> int:
        return random.choice(self.numsList)
