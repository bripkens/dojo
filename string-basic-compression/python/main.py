def toString(list):
  return ''.join(str(i) for i in list)

def compress(s):
  if len(s) == 1: return s

  previousChar = None
  countPreviousChar = 0
  compressedChars = [None] * len(s)
  compressedCharIndex = 0

  for c in s:
    if c == previousChar or previousChar is None:
      previousChar = c
      countPreviousChar += 1
    else:
      compressedChars[compressedCharIndex] = previousChar
      compressedChars[compressedCharIndex + 1] = countPreviousChar
      compressedCharIndex += 2

      previousChar = c
      countPreviousChar = 1

      # Check whether the next part which should be compressed will fit
      if compressedCharIndex + 2 > len(s):
        return s

  compressedChars[compressedCharIndex] = previousChar
  compressedChars[compressedCharIndex + 1] = countPreviousChar
  compressedCharIndex += 2

  if compressedCharIndex < len(compressedChars):
    return toString(compressedChars[0:compressedCharIndex])

  return toString(compressedChars)

if __name__ == '__main__':
  assert compress("a") == "a"
  assert compress("aabcccccaaa") == "a2b1c5a3"
  assert compress("Non compressable string.") == "Non compressable string."
