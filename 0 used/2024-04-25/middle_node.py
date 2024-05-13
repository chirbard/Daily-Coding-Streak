def find_middle(linked_list):
  left = linked_list.get_head_node()
  rigth = linked_list.get_head_node()
  move_left = False

  while rigth:
    rigth = rigth.get_next_node()
    if move_left:
      left = left.get_next_node()
      move_left = False
    else:
      move_left = True
  return left