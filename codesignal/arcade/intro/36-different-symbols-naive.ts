function solution(s: string): number {
  const uniqueChars = new Set();
  for (const char of s) {
    uniqueChars.add(char);
  }
  return uniqueChars.size;
}
