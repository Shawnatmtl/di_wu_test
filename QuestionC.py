from datetime import datetime
from time import *

"""

I read about what is LRU, 
for my understand LRU means
when we set a new value, we check 
                        if the cached size < cache size and key not in the cached
                            then we cache this value
                        else if the cached size == cached size 
                            then pop out the the old one and cache the value
                        else the key in the cached
                            update the cached timestamp
when we get a key and value, we check if the key in the cached and the within the expiration ,we get the value from cache

"""
class LRUcache:
    def __init__(self, size=3, expiration=3):
        self.cache = {}
        self.keys = []
        self.size = size
        self.expiration = expiration
        self.timestamp = {}

    def get(self, key):
        if key in self.cache and (datetime.now()- self.timestamp[key]).seconds <= self.expiration:
            print( (datetime.now()- self.timestamp[key]).seconds <= self.expiration)
            self.keys.remove(key)
            self.keys.insert(0, key)
            return "cacche(value:{} timestamp{})".format(self.cache[key], self.timestamp[key])
        else:
            return None

    def set(self, key, value):
        if key in self.cache:
            self.keys.remove(key)
            self.keys.insert(0, key)
            self.cache[key] = value
            self.timestamp[key]  = datetime.now()
            print(self.timestamp[key])
        elif len(self.keys) == self.size:
            old = self.keys.pop()
            self.cache.pop(old)
            self.timestamp.pop(old)
            self.keys.insert(0, key)
            self.cache[key] = value
            self.timestamp[key] = datetime.now()
            print(self.timestamp[key])
        else:
            self.keys.insert(0, key)
            self.cache[key] = value
            self.timestamp[key] = datetime.now()
            print(self.timestamp[key])

if __name__ == '__main__':
    test = LRUcache()
    test.set('a',2)
    sleep(1)
    test.set('b',2)
    sleep(2)
    test.set('c',2)
    sleep(3)
    test.set('d',2)
    sleep(4)
    test.set('e',2)
    sleep(5)
    test.set('f',2)
    sleep(1)
    print(test.get('c'))
    print(test.get('b'))
    print(test.get('a'))
    print(test.get('f'))
    sleep(2)
    print(test.get('d'))
    sleep(5)
    print(test.get('e'))
    sleep(1)
    print(test.get('e'))