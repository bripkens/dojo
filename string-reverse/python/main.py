def reverse(chars):
  left = 0
  right = len(chars) - 1

  while left < right:
    leftChar = chars[left]
    chars[left] = chars[right]
    chars[right] = leftChar

    left += 1
    right -= 1

  return chars

if __name__ == '__main__':
  assert reverse(['A', 'B', 'C']) == ['C', 'B', 'A']
  assert reverse(['A', 'B']) == ['B', 'A']
