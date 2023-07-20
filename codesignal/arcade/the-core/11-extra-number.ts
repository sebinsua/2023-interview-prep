function solution(a: number, b: number, c: number): number {
  if (a === b) {
    return c;
  }
  if (a === c) {
    return b;
  }
  if (b === c) {
    return a;
  }

  throw new Error(
    "It should have been guaranteed that at least two of the integers would be equal."
  );
}
