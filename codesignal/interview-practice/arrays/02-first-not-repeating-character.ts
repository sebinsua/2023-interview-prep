function solution(s: string): string {
  let map = new Map<string, number | undefined>();
  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    map.set(char, !map.has(char) ? i : undefined);
  }

  const nonRepeatingElement = Array.from(map.entries())
    .filter(([char, index]) => index !== undefined)
    .sort(([, index]) => index)
    .shift();

  if (nonRepeatingElement) {
    const [nonRepeatingChar] = nonRepeatingElement;
    return nonRepeatingChar;
  }

  return "_";
}
