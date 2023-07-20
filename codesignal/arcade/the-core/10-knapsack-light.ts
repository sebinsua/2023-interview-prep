function solution(
  value1: number,
  weight1: number,
  value2: number,
  weight2: number,
  maxW: number
): number {
  if (weight1 + weight2 <= maxW) {
    return value1 + value2;
  }

  let maxValue = 0;
  if (weight1 <= maxW) {
    maxValue = Math.max(maxValue, value1);
  }
  if (weight2 <= maxW) {
    maxValue = Math.max(maxValue, value2);
  }

  return maxValue;
}
