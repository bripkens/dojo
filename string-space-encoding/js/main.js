var assert = require('assert');

function encodeWhitespace(chars) {
  var rightSideIndex = chars.length - 1,
    firstNonWhitespaceCharFound = false;

  for (var i = chars.length - 1; i >= 0; i--) {
    var c = chars[i],
      isWhitespace = c == ' ';

    if (isWhitespace && firstNonWhitespaceCharFound) {
      chars[rightSideIndex--] = '0';
      chars[rightSideIndex--] = '2';
      chars[rightSideIndex--] = '%';
    } else if (!isWhitespace) {
      chars[rightSideIndex--] = c;
      firstNonWhitespaceCharFound = true;
    }
  }

  return chars;
}

assert.deepEqual(encodeWhitespace("Mr John Smith    ".split('')), "Mr%20John%20Smith".split(''))