# Binary search with pointers
#
# def binary_search(sorted_list, left_pointer, right_pointer, target):
#   # this condition indicates we've reached an empty "sub-list"
#   if left_pointer >= right_pointer:
#     return "value not found"
	
#   # We calculate the middle index from the pointers now
#   mid_idx = (left_pointer + right_pointer) // 2
#   mid_val = sorted_list[mid_idx]

#   if mid_val == target:
#     return mid_idx
#   if mid_val > target:
#     # we reduce the sub-list by passing in a new right_pointer
#     return binary_search(sorted_list, left_pointer, mid_idx, target)
#   if mid_val < target:
#     # we reduce the sub-list by passing in a new left_pointer
#     return binary_search(sorted_list, mid_idx + 1, right_pointer, target)
  
# values = [77, 80, 102, 123, 288, 300, 540]
# start_of_values = 0
# end_of_values = len(values)
# result = binary_search(values, start_of_values, end_of_values, 288)

# print("element {0} is located at index {1}".format(288, result))



# define binary_search()
def binary_search(sorted_list, target):
  if not sorted_list:
    return 'value not found'
  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]
  if mid_val == target:
    return mid_idx
  if mid_val > target:
    left_half = sorted_list[:mid_idx]
    return binary_search(left_half, target)
  if mid_val < target:
    right_half = sorted_list[mid_idx + 1:]
    result = binary_search(right_half, target)
    if result == "value not found":
      return result
    return result + mid_idx + 1

# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search(sorted_values, 16))