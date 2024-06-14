from LinkedList import *

def reverse_linked_list(linked_list, our_recursive_linked_list=None):
  if not linked_list: # Case where linked list is empty.
    return linked_list
  if not our_recursive_linked_list: # Before our recursive calls we create the new linked list.
    our_recursive_linked_list = make_linked_list([linked_list.data])
  if not linked_list.next: # Base case.
    return our_recursive_linked_list
  new_head = make_linked_list([linked_list.next.data])
  new_head.next = our_recursive_linked_list
  return reverse_linked_list(linked_list.next, new_head)

print("Original")
demo_list = make_linked_list([4,8,7,3])
demo_list.print_linked_list()
print("Reversed")
reverse = reverse_linked_list(demo_list)
reverse.print_linked_list()
print("Original Unchanged")
demo_list.print_linked_list()
