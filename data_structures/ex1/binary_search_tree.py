class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    pass    

  def breadth_first_for_each(self, cb):
    pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value

  def depth_first_for_each(self, cb):
    stack = []
    stack.append({'tree':self,'left_bad':True,'right_bad':True})
    cb(stack[len(stack)-1]['tree'].value)
    while(len(stack)>0):
      if stack[len(stack)-1]['left_bad']:
        next = stack[len(stack)-1]['tree'].left
        if next == None:
          stack[len(stack)-1]['left_bad'] = False
          continue
        stack[len(stack)-1]['left_bad'] = False
        stack.append({'tree':next,'left_bad':True,'right_bad':True})
        cb(stack[len(stack)-1]['tree'].value)
      elif stack[len(stack)-1]['right_bad']:
        next = stack[len(stack)-1]['tree'].right
        if next == None:
          stack[len(stack)-1]['right_bad'] = False
          continue
        stack[len(stack)-1]['right_bad'] = False
        stack.append({'tree':next,'left_bad':True,'right_bad':True})
        cb(stack[len(stack)-1]['tree'].value)
      else:
        stack.pop()
      