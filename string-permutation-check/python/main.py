CHAR_COUNT = 65535

# Time: O(2*n + m) => O(N)
# Space: O(1)
def isPermutation(s1, s2):
  if not len(s1) == len(s2): return False

  chars = [0] * CHAR_COUNT

  for c in s1:
    chars[ord(c)] += 1

  for c in s2:
    chars[ord(c)] -= 1

  for c in chars:
    if not c == 0:
      return False

  return True

if __name__ == '__main__':
  assert isPermutation("ABCDE", "DBCAE")
  assert not isPermutation("ABCDE", "DBCAEF")
