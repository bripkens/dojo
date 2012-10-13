var assert = require('assert');

function isPermutation(s1, s2) {
  if (s1.length != s2.length) return false;

  var chars = [], i;
  for (i = 0; i < s1.length; i++) {
    chars[s1.charCodeAt(i)]++;
  }

  for (i = 0; i < s2.length; i++) {
    chars[s2.charCodeAt(i)]--;
  }

  for (i = 0; i < chars.length; i++) {
    if (chars[i] > 0) return false;
  }

  return true;
}

assert(isPermutation('ABCDE', 'DAEBC'));
assert(!isPermutation('ABCDE', 'DAEBCF'));
assert(!isPermutation('ABCDE', 'DAEEBC'));