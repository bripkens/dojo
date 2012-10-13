var assert = require('assert');

function reverse(chars) {
  var left = 0,
    right = chars.length - 1;

  while (left < right) {
    var leftChar = chars[left];

    chars[left] = chars[right];
    chars[right] = leftChar;

    left++;
    right--;
  }

  return chars;
}

assert.deepEqual(reverse(['A', 'B', 'C', 'D']), ['D', 'C', 'B', 'A']);
assert.deepEqual(reverse(['A', 'B', 'C']), ['C', 'B', 'A']);
assert.deepEqual(reverse(['A', 'B']), ['B', 'A']);
assert.deepEqual(reverse(['A']), ['A']);