class HashTable:
    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.M = size
    def hash(self, key):
        return key % self.M
    def insert(self, key):
        address = self.hash(key)
        if self.data[address] == None:
            self.data[address] = key
        else:
            while self.data[address] != None:
                address = (address + 1) % self.M
            self.data[address] = key
    def isExist(self, key):
        address = self.hash(key)
        start = address
        if self.data[address] == key:
            return True
        else:
            while self.data[address] != key:
                address = (address + 1) % self.M
                if address == start or self.data[address]==None:
                    return False
            return True
    def search(self, key):
        address = self.hash(key)
        if self.isExist(key):
            while self.data[address] != key:
                address = (address + 1) % self.M
            return address
        else:
            return None    
    def v(self):
        print(self.data)
h = HashTable(8)
n = int(input())
for i in range(n):
    h.insert(int(input()))
    h.v()
print(h.search(1))
print(h.search(2))  
