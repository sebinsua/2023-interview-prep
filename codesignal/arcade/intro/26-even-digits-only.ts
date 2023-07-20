function solution(n: number): boolean {
  const nStr = String(n);
  return nStr.split("").every((char) => parseInt(char) % 2 === 0);
}
