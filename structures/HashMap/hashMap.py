from __future__ import division

class KVPair(object):
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.collisions = []

    def __iter__(self):
        yield self.key, self.value
        for value in self.collisions:
            yield value.key, value.value

    def __eq__(self, other):
        return self.value == other

    def add(self, key, value):
        if value == self.value:
            self.value = value
            self.key = key
            return
        for index,collision in enumerate(self.collisions):
            if value == collision:
                self.collisions[index].add(key, value)
                return
        self.collisions.append(KVPair(key, value))

class HashMap(object):
    
    def __init__(self, size=100):
        self.table = [None for _ in xrange(size)]
        self.size = size
        self.count = 0
        self.keys = []
    
    def __iter__(self):
        for k,_ in self.items():
            yield k

    def _expand(self):
        table = HashMap(size=self.size*2)
        for k,v in self.items():
            table.add(k, v)
        self = table

    def items(self):
        index = 0
        while index < len(self.keys):
            hashCode = self._hash(self.keys[index])
            pair = self.table[hashCode]
            if pair is None:
                self.keys.pop(index)
            else:
                for key,value in pair:
                    yield key,value
                index += 1

    @property
    def fillFactor(self):
        pass
    
    @fillFactor.getter
    def fillFactor(self):
        return self.count / self.size
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def get(self, key):
        obj = self.table[self._hash(key)]
        return obj.value if obj is not None else None
    
    def add(self, key, value):
        hashCode = self._hash(key)
        pair = self.table[hashCode]
        if pair is None:
            if self.fillFactor >= 0.5:
                self._expand()
            self.table[hashCode] = KVPair(key, value)
            self.keys.append(key)
        else:
            pair.add(key, value)
    
lol = HashMap()
for i in range(51):
    lol.add(str(i),i)
for k,v in lol.items():
    print (k,v)