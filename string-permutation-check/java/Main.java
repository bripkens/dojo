public class Main {

  public static boolean isPermutation(String s1, String s2) {
    if (s1.length() != s2.length()) return false;

    int[] chars = new int[65536];

    for (int i = 0; i < s1.length(); i++) {
      chars[s1.charAt(i)]++;
    }

    for (int i = 0; i < s2.length(); i++) {
      chars[s2.charAt(i)]--;
    }

    for (int i = 0; i < chars.length; i++) {
      if (chars[i] > 0) return false;
    }

    return true;
  }

  public static void main(String[] args) {
    assert !isPermutation("ABCDE", "ABBCD");
    assert isPermutation("ABCDE", "ABCDE");
    assert isPermutation("ABCDE", "EDBAC");
  }
}
