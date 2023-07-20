function solution(n: number): number {
  const nStr = String(n);

  let max = 0;
  for (let i = 0; i < nStr.length; i++) {
    max = Math.max(
      max,
      parseInt(`${nStr.substring(0, i)}${nStr.substring(i + 1)}`)
    );
  }

  return max;
}
