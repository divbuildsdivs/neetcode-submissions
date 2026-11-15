class MyHashSet:

    def __init__(self):
        self.arr = []
        self.indexMap = {}
        

    def add(self, key: int) -> None:
        if key not in self.indexMap or self.indexMap[key] == -1:
            self.arr.append(key)
            self.indexMap[key] = len(self.arr) - 1
        

    def remove(self, key: int) -> None:
        if key in self.indexMap and self.indexMap[key] != -1:
            temp = self.arr[-1]
            self.indexMap[temp] = self.indexMap[key]
            self.indexMap[key] = -1

            
        

    def contains(self, key: int) -> bool:
        return key in self.indexMap and self.indexMap[key] != -1
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)