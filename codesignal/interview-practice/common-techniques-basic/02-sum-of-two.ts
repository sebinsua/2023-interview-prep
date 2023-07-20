function solution(a: number[], b: number[], v: number): boolean {
  const aSet = new Set(a);
  const bSet = new Set(b);
  for (let aValue of aSet) {
    if (bSet.has(v - aValue)) {
      return true;
    }
  }

  return false;
}
