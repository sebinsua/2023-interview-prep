function solution(a: number, b: number): boolean {
  if (a === b) {
    return false;
  }

  if (a < b && (b - a) % 2 === 0) {
    return false;
  }

  return true;
}
