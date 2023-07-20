function solution(inputArray: number[], k: number): number {
  let maxSum = -Infinity;
  let currentSum = 0;

  for (let i = 0; i < inputArray.length; i++) {
    currentSum += inputArray[i];

    if (i >= k) {
      currentSum -= inputArray[i - k];
    }

    if (i >= k - 1) {
      maxSum = Math.max(maxSum, currentSum);
    }
  }

  return maxSum;
}
