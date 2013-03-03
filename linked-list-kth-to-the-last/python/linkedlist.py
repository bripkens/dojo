class Node(object):
  value = None
  next = None

  def __init__(self, value):
    self.value = value

  def add(self, value):
    new_node = Node(value)
    self.next = new_node
    return self.next


def to_string(node):
  values = []
  while not node is None:
    values.append(str(node.value))
    node = node.next
  return ','.join(values)


def get_dummy_list():
  current = head = Node(1)
  current = current.add(2)
  current = current.add(3)
  current = current.add(2)
  current = current.add(4)
  current = current.add(1)
  return head