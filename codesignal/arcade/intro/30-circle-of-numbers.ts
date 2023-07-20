function solution(n: number, firstNumber: number): number {
  const midpoint = Math.round(n / 2);
  return (midpoint + firstNumber) % n;
}
