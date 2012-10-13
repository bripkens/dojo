var assert = require('assert'),
  charSetSize = 256; // restriction to ASCII

function allUnique(s) {
  if (s.length > charSetSize) return false;

  var foundChars = [];
  for (var i = 0; i < s.length; i++) {
    var charCode = s.charCodeAt(i),
      charFound = foundChars[charCode];
    if (charFound === true) {
      return false;
    }

    foundChars[charCode] = true;
  }

  return true;
};


assert(allUnique('abcde'));
assert(!allUnique('abade'));
assert(!allUnique('abcda'));
assert(!allUnique('bacdae'));
