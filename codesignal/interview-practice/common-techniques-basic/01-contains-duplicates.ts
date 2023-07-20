function solution(a: number[]): boolean {
  const s = new Set(a);
  return s.size !== a.length;
}
