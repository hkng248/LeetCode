class MyHashMap:
    n = None 
    
    def __init__(self):
        self.n = [-1]*1000000
        """
        Initialize your data structure here.
        """
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.n[key] = value 

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.n[key]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.n[key]=-1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
