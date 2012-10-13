public class Main {

  public static char[] encodeWhitespace(char[] chars) {
    boolean firstNonWhitespaceCharFound = false;
    int rightSideIndex = chars.length - 1;

    for (int i = chars.length - 1; i >= 0; i--) {
      char c = chars[i];

      boolean isWhitespace = c == ' ';
      if (isWhitespace && firstNonWhitespaceCharFound) {
        chars[rightSideIndex--] = '0';
        chars[rightSideIndex--] = '2';
        chars[rightSideIndex--] = '%';
      } else if (!isWhitespace) {
        firstNonWhitespaceCharFound = true;
        chars[rightSideIndex--] = c;
      }
    }

    return chars;
  }

  public static boolean deepEqual(char[] a1, char[] a2) {
    if (a1.length != a2.length) return false;

    for (int i = 0; i < a1.length; i++) {
      if (a1[i] != a2[i]) {
        return false;
      }
    }

    return true;
  }

  public static void main(String[] args) {
    assert deepEqual(encodeWhitespace("Mr John Smith    ".toCharArray()), "Mr%20John%20Smith".toCharArray());
  }
}
