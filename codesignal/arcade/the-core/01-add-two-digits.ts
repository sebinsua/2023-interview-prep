function solution(n: number): number {
  return String(n)
    .split("")
    .map((char) => parseInt(char))
    .reduce((acc, digit) => acc + digit, 0);
}
