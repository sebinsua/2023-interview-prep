function solution(a: number[]): number {
  const map = new Map<number, true>();
  for (let v of a) {
    if (map.has(v)) {
      return v;
    }
    map.set(v, true);
  }

  return -1;
}
