function counter(str: string): Map<string, number> {
  const chars = str.split("");
  const counts = new Map<string, number>();
  for (const char of chars) {
    counts.set(char, (counts.has(char) ? counts.get(char)! : 0) + 1);
  }
  return counts;
}

function solution(s1: string, s2: string): number {
  const s1Counts = counter(s1);
  const s2Counts = counter(s2);

  // We choose the string with the least number of unique characters
  // This is a performance trick so we can avoid iterating over characters
  // that do not even exist in the other string.
  let a: Map<string, number>;
  let b: Map<string, number>;
  if (s1Counts.size >= s2Counts.size) {
    a = s2Counts;
    b = s1Counts;
  } else {
    a = s1Counts;
    b = s2Counts;
  }

  let totalCommonCharacters = 0;
  for (let [char, count] of a.entries()) {
    if (b.has(char)) {
      totalCommonCharacters += Math.min(count, b.get(char));
    }
  }

  return totalCommonCharacters;
}
