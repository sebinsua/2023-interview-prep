function solution(deposit: number, rate: number, threshold: number): number {
  let n = 0;

  let currentValue = deposit;
  if (currentValue >= threshold) {
    return n;
  }

  const percentageRate = (100 + rate) / 100;
  while (currentValue < threshold) {
    n++;
    currentValue *= percentageRate;
  }

  return n;
}
