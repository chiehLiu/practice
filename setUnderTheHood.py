class MySet:
  def __init__(self, size=1000):
    self.size = size
    self.buckets = [[] for _ in range(size)]
  
  def _hash(self, key):
    return hash(key) % self.size
  
  def add(self, key):
    idx = self._hash(key)
    bucket = self.buckets[idx]
    if key not in bucket:
      bucket.append(key)
  
  def contains(self, key):
    idx = self._hash(key)
    return key in self.buckets[idx]
  
  def remove(self, key):
    idx = self._hash(key)
    bucket = self.buckets[idx]
    if key in bucket:
      bucket.remove(key)
  

s = MySet()
s.add(1)
s.add(2)
print(s.contains(1))
print(s.contains(3))
s.remove(1)
print(s.contains(1))