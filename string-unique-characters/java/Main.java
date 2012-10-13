public class Main {

  // in place analysis, no additional data structure used for the analysis.
  // Time: O(n^2) as String#indexOf is O(n)
  // Space: O(n) when including input
  public static boolean allUniqueCharacters(String s) {
    char[] chars = s.toCharArray();

    for (int i = 0; i < chars.length; i++) {
      int nextCharIndex = i+1;
      if (nextCharIndex < chars.length && s.indexOf(chars[i], nextCharIndex) != -1) {
        return false;
      }
    }

    return true;
  }

  // Time: O(n)
  // Space: O(1)
  public static boolean allUniqueCharactersConstant(String s) {
    if (s.length() > 65536) return false;

    char[] chars = s.toCharArray();
    boolean[] foundChars = new boolean[65536];

    for (char eachChar : chars) {
      int i = Character.getNumericValue(eachChar);

      if (foundChars[i]) {
        return false;
      }

      foundChars[i] = true;
    }

    return true;
  }

  public static void main(String[] args) {
    System.out.println("Testing 'allUniqueCharacters'");
    assert Main.allUniqueCharacters("abcde");
    assert !Main.allUniqueCharacters("abade");
    assert !Main.allUniqueCharacters("abeda");
    assert !Main.allUniqueCharacters("fbeaa");

    System.out.println("Testing 'allUniqueCharactersConstant'");
    assert Main.allUniqueCharactersConstant("abcde");
    assert !Main.allUniqueCharactersConstant("abade");
    assert !Main.allUniqueCharactersConstant("abeda");
    assert !Main.allUniqueCharactersConstant("fbeaa");

    System.out.println("Great success!");
  }
}