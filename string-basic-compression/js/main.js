var assert = require('assert');


function compress(s) {
  if (s.length < 3) return s;

  var prevChar = s.charAt(0),
    countPrevChar = 1,
    compressedChars = [],
    i,
    currChar;

  function addCompressedChar() {
    compressedChars.push(prevChar);
    compressedChars.push(countPrevChar);
  }

  for (i = 1; i < s.length; i++) {
    currChar = s.charAt(i);

    if (prevChar === currChar) {
      countPrevChar++;
    } else {
      addCompressedChar();
      prevChar = currChar;
      countPrevChar = 1;
    }
  }

  addCompressedChar();

  if (compressedChars.length >= s.length) {
    return s;
  }

  return compressedChars.join('');
};

assert.equal(compress('a'), 'a');
assert.equal(compress('aa'), 'aa');
assert.equal(compress('ab'), 'ab');
assert.equal(compress('aaa'), 'a3');
assert.equal(compress('aabba'), 'aabba');
assert.equal(compress('aabbbba'), 'a2b4a1');