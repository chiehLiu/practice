class MySet:
  def __init__(self, size=1000):
    self.size = size
    self.buckets = [[] for _ in range(size)]
  
  def _hash(self, key):
    # hash is a build-in funciton in Python that returns a hash value of an object
    # and we use modulo to ensure the index is within the bounds of the buckets
    return hash(key) % self.size
  
  def add(self, key):
    idx = self._hash(key)
    bucket = self.buckets[idx]

    # this is the place where we check if the key is already in the bucket!
    if key not in bucket:
      bucket.append(key)
  
  def contains(self, key):
    idx = self._hash(key)
    return key in self.buckets[idx]
  
  def remove_key(self, key):
    idx = self._hash(key)
    bucket = self.buckets[idx]

    # the remove method is build-in in Python
    # it removes the first occurrence of the value in the list
    # if the value is not found, it raises a ValueError
    # so we check if the key is in the bucket before removing it
    if key in bucket:
      bucket.remove(key)
  

s = MySet()
s.add(1)
s.add(2)
print(s.contains(1))
print(s.contains(3))
s.remove_key(1)
print(s.contains(1))