def rotate(m):
  width = len(m)
  height = len(m[0])

  newMatrix = [[0] * height for h in range(width)]

  for y, r in enumerate(m):
    for x, v in enumerate(r):
      newX = width - y - 1
      #print "New X position for %d is %d" % (v, newX);
      newY =  x
      print "New Y position for %d is %d" % (v, newY);
      newMatrix[newY][newX] = v

  return newMatrix

if __name__ == '__main__':
  assert rotate([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]) == [
      [7, 4, 1],
      [8, 5, 2],
      [9, 6, 3]
    ]

  assert rotate([
      [1,  2,  3,  4],
      [5,  6,  7,  8],
      [9, 10, 11, 12],
      []
    ]) == [
      [ 9, 5, 1],
      [10, 6, 2],
      [11, 7, 3],
      [12, 8, 4]
    ]
