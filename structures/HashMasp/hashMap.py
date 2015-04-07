from __future__ import division

class KVPair(object):
    def __init__(self, key, value, root=False):
        self.value = value
        self.key = key
        self.collisions = []

    def __iter__(self):
        yield self.key, self.value
        for value in self.collisions:
            yield value.key, value.value

    def __eq__(self, other):
        return self.value == other

    def keys(self):
        yield self.key
        for collision in self.collisions:
            yield collision.key
    
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
    
    def __init__(self):
        self._sizes = (size for size in (53,
                    97,
                    193,
                    389,
                    769,
                    1543,
                    3079,
                    6151,
                    12289,
                    24593,
                    49157,
                    98317,
                    196613,
                    393241,
                    786433,
                    1572869,
                    3145739,
                    6291469,
                    12582917,
                    25165843,
                    50331653,
                    100663319,
                    201326611,
                    402653189,
                    805306457,
                    1610612741)
                    )
        self.size = self.nextSize
        self.table = [None for _ in xrange(self.size)]
        self.count = 0
        self.keys = []
    
    def __iter__(self):
        for k,_ in self.items():
            yield k

    def _expand(self):
        tmp = self
        self.size = self.nextSize
        self.table = [None for _ in xrange(self.size)]
        self.keys = []
        self.count = 0
        for k,v in tmp.items():
            self.add(k, v)

    @property
    def nextSize(self):
        try:
            return next(self._sizes)
        except:
            raise Exception("Hash table has reached max size.")

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
    def loadFactor(self):
        return self.count / self.size
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def get(self, key):
        obj = self.table[self._hash(key)]
        return obj.value if obj is not None else None
    
    def add(self, key, value):
        if self.loadFactor >= 0.5:
            self._expand()
        hashCode = self._hash(key)
        pair = self.table[hashCode]
        if pair is None:
            self.table[hashCode] = KVPair(key, value)
            self.keys.append(key)
        else:
            pair.add(key, value)
        self.count += 1
    
lol = HashMap()
for i in range(27):
    lol.add(str(i),i)
print (lol.size)