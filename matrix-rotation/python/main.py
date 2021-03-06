def rotate(m):
  height = len(m)
  width = len(m[0])

  newMatrix = [[0] * height for h in range(width)]

  for y, r in enumerate(m):
    for x, v in enumerate(r):
      newX = height - y - 1
      newY =  x

      newMatrix[newY][newX] = v

  return newMatrix

def verify(fn):
  assert fn([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]) == [
      [7, 4, 1],
      [8, 5, 2],
      [9, 6, 3]
    ]

  assert fn([
      [ 1,  2,  3,  4],
      [ 5,  6,  7,  8],
      [ 9, 10, 11, 12],
      [13, 14, 15, 16]
    ]) == [
      [13,  9, 5, 1],
      [14, 10, 6, 2],
      [15, 11, 7, 3],
      [16, 12, 8, 4]
    ]

  assert fn([
      [ 1,  2,  3,  4],
      [ 5,  6,  7,  8],
      [ 9, 10, 11, 12]
    ]) == [
      [ 9, 5, 1],
      [10, 6, 2],
      [11, 7, 3],
      [12, 8, 4]
    ]

if __name__ == '__main__':
  verify(rotate)