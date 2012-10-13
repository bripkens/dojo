NUM_CHARACTERS = 256

def allUnique(str):
  if len(str) > NUM_CHARACTERS: return False

  checker = [False]*NUM_CHARACTERS
  for char in str:
    num = ord(char)

    if checker[num]:
      return False

    checker[num] = True

  return True

if __name__ == '__main__':
  assert allUnique("abcde")
  assert not allUnique("abade")
  assert not allUnique("abada")
  assert not allUnique("bada")