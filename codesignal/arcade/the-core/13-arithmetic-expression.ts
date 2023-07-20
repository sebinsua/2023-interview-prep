function solution(a: number, b: number, c: number): boolean {
  if (a + b === c) {
    return true;
  }
  if (a - b === c) {
    return true;
  }
  if (a * b === c) {
    return true;
  }
  if (b > 0 && a / b === c) {
    return true;
  }
  return false;
}
