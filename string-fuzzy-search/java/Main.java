import java.util.Locale;

public class Main {

  public static void main(String[] args) {
    assert true;

    Matcher matcher = new Matcher("majs");

    assert matcher.match("majs") == 0;
    assert matcher.match("foo") == -1;
    assert matcher.match("main.js") > 0;
    assert matcher.match("main.js") < matcher.match("main.py") &&
      matcher.match("main.py") < matcher.match("Foobar.java");
  }

  private static class Matcher {
    private final String query;
    private final int[] counts;

    private Matcher(String query) {
      this.query = query;
      this.counts = getCharacterCounts(query);
    }

    private int[] getCharacterCounts(String s) {
      int[] counts = new int[65536];
      String ls = s.toLowerCase(Locale.ENGLISH);
      for (int i = 0; i < ls.length(); i++) {
        counts[ls.charAt(i)]++;
      }
      return counts;
    }

    private int match(String term) {
      if (query.equalsIgnoreCase(term)) {
        return 0;
      }

      int[] otherCounts = getCharacterCounts(term);
      int totalDifference = 0;
      boolean oneMatchFound = false;

      for (int i = 0; i < counts.length; i++) {
        int c = counts[i];
        int oc = otherCounts[i];

        oneMatchFound |= c > 0 && oc > 0;
        totalDifference += Math.abs(c - oc);
      }

      if (oneMatchFound) {
        return totalDifference;
      } else {
        return -1;
      }
    }
  }
}
