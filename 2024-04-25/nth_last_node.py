def nth_last_node(linked_list, n):
  remove_me = None
  tail = linked_list.get_head_node()
  count = 1

  while tail:
    tail = tail.get_next_node()
    count += 1

    if count > n:
      if remove_me is None:
        remove_me = linked_list.get_head_node()
      else:
        remove_me = remove_me.get_next_node()
  return remove_me