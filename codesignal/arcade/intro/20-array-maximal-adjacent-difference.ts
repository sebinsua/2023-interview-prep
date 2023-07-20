function solution(inputArray: number[]): number {
  let max = 0;
  let previous;
  for (const n of inputArray) {
    const abs = Math.abs(n - previous);
    if (previous !== undefined && abs) {
      max = Math.max(max, abs);
    }
    previous = n;
  }

  return max;
}
