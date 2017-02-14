import numpy as np

class Node:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


def print_path(root):

  rightpath = []
  leftpath = []
  path = []
  
  if root is None:
    return []
    
  if (root.right is None) and (root.left is None):
    return [root.val]
  if root.right:
    print(root.right.val)
    rightpath = [root.val] + print_path(root.right)
  if root.left:
    print(root.left.val)
    leftpath = [root.val] + print_path(root.left)
    
  print(rightpath, leftpath)
    
  return argmax(rightpath, leftpath)

def argmax(lst1, lst2):
  return lst1 if len(lst1) > len(lst2) else lst2
  
  
def calculate_path(root):

    # left - arr[0]
    # right - arr[1]
    # max - arr[2]
    arr = [0, 0, 0]

    if root is None:
        return arr
    else:
        #print(root.val)
        left_res = calculate_path(root.left)
        right_res = calculate_path(root.right)

        left_len = left_res[0] + 1
        right_len = right_res[1] + 1
 
        max_len = np.amax([max(left_len, right_len), max(left_res[2], right_res[2])]) 
        arr = [left_len, right_len, max_len]
        
        return arr
        
    


root_node = Node('a')
root_node.left = Node('b')
root_node.left.left = Node('h')
root_node.left.right = Node('z')
root_node.left.left.left = Node('j')
root_node.left.left.right = Node('k')
root_node.left.left.right.left = Node('o')
root_node.left.left.right.right = Node('p')
root_node.left.left.right.left.left = Node('r')
root_node.left.left.right.left.right = Node('s')
root_node.left.left.right.left.left.left = Node('t')
root_node.left.left.right.left.left.right = Node('u')
root_node.left.left.right.left.left.left.left = Node('v')
root_node.left.left.right.left.left.left.right = Node('w')

root_node.right = Node('c')
root_node.right.right = Node('f')
root_node.right.left = Node('g')

print calculate_path(root_node)[2] - 1
