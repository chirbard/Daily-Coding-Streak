# Iterative from Codecademy
# def depth(tree):
#   result = 0
#   # our "queue" will store nodes at each level
#   queue = [tree]
#   # loop as long as there are nodes to explore
#   while queue:
#     # count the number of child nodes
#     level_count = len(queue)
#     for child_count in range(0, level_count):
#       # loop through each child
#       child = queue.pop(0)
#      # add its children if they exist
#       if child["left_child"]:
#         queue.append(child["left_child"])
#       if child["right_child"]:
#         queue.append(child["right_child"])
#     # count the level
#     result += 1
#   return result

# My Recursive solution
def depth(tree):
  # Mul on root millel on kolm võtit.
  # Vasak ja parem laps on võtmed, mis on ise nagu root oma kolme võtmega.
  # Ma pean lugema ainult vasakuid lapsi.
  # Kui data on null siis returni 0.
  # Kui vasak laps on null siis returni 1.
  # Kutsu välja sama funktsioon vasaku lapse peal ja liida 1.
  if tree['data'] == None: return 0
  if tree['left_child'] == None: return 1
  return 1 + depth(tree['left_child'])

# HELPER FUNCTION TO BUILD TREES
def build_bst(my_list):
  if len(my_list) == 0:
    return None

  mid_idx = len(my_list) // 2
  mid_val = my_list[mid_idx]

  tree_node = {"data": mid_val}
  tree_node["left_child"] = build_bst(my_list[ : mid_idx])
  tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

  return tree_node

# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 

# test cases
print(depth(tree_level_1) == 1)
print(depth(tree_level_2) == 2)
print(depth(tree_level_4) == 4)