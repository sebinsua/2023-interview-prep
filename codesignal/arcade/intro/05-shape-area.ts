// The sequence is:
//
// 1: 1
// 2: 5
// 3: 13
// 4: 25
//
// The jump is 4, 8, and then 12.
// e.g. 4 * (n - 1)
function solution(n: number): number {
  if (n === 1) {
    return n;
  }

  return solution(n - 1) + 4 * (n - 1);
}
