from linkedlist import get_dummy_list
from linkedlist import to_string

def remove(node):
  node.value = node.next.value
  node.next = node.next.next


head = get_dummy_list()
remove(head.next)
assert '1,3,2,4,1' == to_string(head)
