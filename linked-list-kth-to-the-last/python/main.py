from linkedlist import get_dummy_list
from linkedlist import to_string


def get_last_values(k, node):
  if node is None:
    return {
      'depth': 0,
      'node': None
    }

  result = get_last_values(k, node.next)
  result['depth'] += 1
  if result['depth'] <= k:
    result['node'] = node

  return result


def get_last_values_iteratively(k, node):
  runner = node
  runner_headstart = 0
  while not runner is None and runner_headstart < k:
    runner = runner.next
    runner_headstart += 1

  if runner_headstart < k:
    return node

  while not runner is None:
    runner = runner.next
    node = node.next

  return node


head = get_dummy_list()
assert '' == to_string(get_last_values(0, head)['node'])
assert '2,4,1' == to_string(get_last_values(3, head)['node'])
assert '1,2,3,2,4,1' == to_string(get_last_values(20, head)['node'])

assert '' == to_string(get_last_values_iteratively(0, head))
assert '2,4,1' == to_string(get_last_values_iteratively(3, head))
assert '1,2,3,2,4,1' == to_string(get_last_values_iteratively(20, head))