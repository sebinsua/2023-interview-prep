function solution(n: number): number {
  let nStr = String(n);
  let degree = 0;
  while (nStr.length !== 1) {
    nStr = String(
      nStr
        .split("")
        .map((d) => parseInt(d))
        .reduce((acc, value) => acc + value, 0)
    );
    degree++;
  }
  return degree;
}
