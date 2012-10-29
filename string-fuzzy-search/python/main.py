def matchFuzzy(query, queryCharCounts, term):
  if query == term:
    return 0

  termCharCounts = getCharCounts(term)

  totalDifference = 0
  oneMatch = False
  for i, c in enumerate(queryCharCounts):
    tc = termCharCounts[i]
    oneMatch = oneMatch or (c > 0 and tc > 0)
    totalDifference += abs(c - tc)

  if not oneMatch:
    return -1

  return totalDifference

def getCharCounts(s):
  charCounts = [0] * 65536

  for c in s.lower():
    charCounts[ord(c)] += 1

  return charCounts

def createFuzzyMatcher(query):
  return lambda term: matchFuzzy(query, getCharCounts(query), term)

if __name__ == '__main__':
  matcher = createFuzzyMatcher('majs')

  # A 100% match is denoted through a 0
  assert matcher('majs') == 0

  # No match is denoted through a -1
  assert matcher('foo') == -1

  # Partial matches are denoted through a value > 0. A small value generally
  # describes the best match
  assert matcher('main.js') > 0

  assert matcher('main.js') < matcher('main.py') < matcher('Foobar.java')