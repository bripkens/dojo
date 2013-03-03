from linkedlist import get_dummy_list
from linkedlist import to_string


def remove_duplicates(node):
  existing_values = set([node.value])

  while not node.next is None:
    next = node.next
    if next.value in existing_values:
      node.next = next.next
    else:
      node = node.next
      existing_values.add(node.value)


def remove_duplicates_constant_memory(node):
  while not node is None:
    before_check = node
    check = node.next

    while not check is None:
      if check.value == node.value:
        before_check.next = check.next
        check = check.next
      else:
        before_check = check
        check = check.next

    node = node.next


head = get_dummy_list()
remove_duplicates(head)
assert to_string(head) == '1,2,3,4'


head = get_dummy_list()
remove_duplicates_constant_memory(head)
assert to_string(head) == '1,2,3,4'