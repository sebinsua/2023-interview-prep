function solution(n: number, m: number): number {
  if (n === 0) {
    return 0;
  }
  return Math.floor(m / n) * n;
}
