# the basic time complexity Analysis:
# 1. addFront(): O(1)
# 2. addRear(): O(1)
# 3. removeFront(): O(1)
# 4. removeRear(): O(1)
# 5. getFront(): O(1)
# 6. getRear(): O(1)
# 7. isEmpty(): O(1)
# 8. size(): O(1)

# the basic space complexity Analysis:
# Basic Deque: O(n) where n is number of elements
class Deque:
  def __init__(self):
    self.items = []
  
  # Add to front
  def addFront(self, item):
    self.items.insert(0, item)
  
  # Add to rear
  def addRear(self, item):
    self.items.append(item)
  
  # Remove from front
  def removeFront(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None
  
  # Remove from rear
  def removeRear(self):
        if not self.isEmpty():
            return self.items.pop()
        return None
  
  # Get front element
  def getFront(self):
      if not self.isEmpty():
          return self.items[0]
      return None
    
  # Get rear element
  def getRear(self):
      if not self.isEmpty():
          return self.items[-1]
      return None
  
  # Check if empty
  def isEmpty(self):
      return len(self.items) == 0
  
  # Get size
  def size(self):
      return len(self.items)

# Example 1: Basic Operations
def example_basic_operations():
  print("Example 1: Basic Operations")
  deque = Deque()

  # Adding elements
  deque.addRear(1) # deque: [1]
  deque.addRear(2) # deque: [1, 2]
  deque.addFront(0) # deque: [0, 1, 2]

  print(f"Deque: {deque.items}") # [0, 1, 2]
  print(f"Front element: {deque.getFront()}") # 0
  print(f"Rear element: {deque.getRear()}") # 2
  print(f"Size: {deque.size()}") # 3

  # Removing elements
  front = deque.removeFront() # deque: [1, 2]
  rear = deque.removeRear() # deque: [1]

  print(f"Removed front: {front}") # 0
  print(f"Removed rear: {rear}") # 2
  print(f"Updated deque: {deque.items}") # [1]

# Example 2: Palindrome Checker using Deque
def is_palindrome(string):
    deque = Deque()

    # Add all characters to deque
    for char in string:
        deque.addRear(char)
      
    while deque.size > 1:
        if deque.removeFront() != deque.removeRear():
            return False
    
    return True

# Example 3: Sliding Window using Deque
def sliding_window_max(arr, k):
    from collections import deque  # Using Python's built-in deque
    result = []
    d = deque()
    
    # Process first k elements
    for i in range(k):
        # Remove smaller elements
        while d and arr[d[-1]] < arr[i]:
            d.pop()
        d.append(i)
    
    # Process remaining elements
    for i in range(k, len(arr)):
        # Add max element from previous window
        result.append(arr[d[0]])
        
        # Remove elements outside window
        while d and d[0] <= i-k:
            d.popleft()
            
        # Remove smaller elements
        while d and arr[d[-1]] < arr[i]:
            d.pop()
            
        d.append(i)
    
    # Add max element of last window
    result.append(arr[d[0]])
    return result

# Let's run our examples
def run_examples():
    # Example 1
    example_basic_operations()
    print("\n" + "="*50 + "\n")
    
    # Example 2
    test_strings = ["radar", "hello", "racecar", "python"]
    print("Example 2: Palindrome Checker")
    for s in test_strings:
        print(f"'{s}' is palindrome: {is_palindrome(s)}")
    print("\n" + "="*50 + "\n")
    
    # Example 3
    print("Example 3: Sliding Window Maximum")
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = sliding_window_max(arr, k)
    print(f"Array: {arr}")
    print(f"Window size: {k}")
    print(f"Maximum in each window: {result}")

run_examples()