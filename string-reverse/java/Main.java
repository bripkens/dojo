public class Main {

  public static char[] reverse(char[] chars) {
    int left = 0, right = chars.length - 1;

    while (left < right) {
      char leftChar = chars[left];
      chars[left] = chars[right];
      chars[right] = leftChar;
      left++;
      right--;
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

  public static char[] toArray(char... chars) {
    return chars;
  }

  public static void main(String[] args) {
    assert deepEqual(reverse(toArray('a', 'b', 'c')),
        toArray('c', 'b', 'a'));
    assert deepEqual(reverse(toArray('a', 'b', 'c', 'd')),
        toArray('d', 'c', 'b', 'a'));
  }
}
