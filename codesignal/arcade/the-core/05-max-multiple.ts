function solution(divisor: number, bound: number): number {
  const mod = bound % divisor;
  return bound - mod;
}
