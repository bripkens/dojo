def encodeSpaces(chars):
  firstNonWhitespaceFound = False
  movedCharIndex = len(chars) - 1

  for i in range(len(chars) - 1, -1, -1):
    char = chars[i]

    isWhitespace = char == ' '
    if isWhitespace and firstNonWhitespaceFound:
      chars[movedCharIndex] = '0'
      chars[movedCharIndex - 1] = '2'
      chars[movedCharIndex - 2] = '%'
      movedCharIndex -= 3
    elif not isWhitespace:
      firstNonWhitespaceFound = True
      chars[movedCharIndex] = char
      movedCharIndex -= 1

  return chars

if __name__ == '__main__':
  assert encodeSpaces(list("Mr John Smith    ")) == list("Mr%20John%20Smith")
