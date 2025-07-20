from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self._cache = OrderedDict()
        self._capacity = capacity

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        value = self._cache.pop(key)
        self._cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._cache.pop(key)
        elif len(self._cache) >= self._capacity:
            self._cache.popitem(last=False)
        self._cache[key] = value


x = LRUCache(2)
x.put(1, 1)
x.put(2, 2)
x.get(1)
x.put(3, 3)
x.get(2)
x.put(4, 4)
x.get(1)
x.get(3)
x.get(4)