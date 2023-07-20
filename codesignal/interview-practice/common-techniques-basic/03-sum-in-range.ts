function moduloBy(n: number, by: number): number {
  return ((n % by) + by) % by;
}

function solution(nums: number[], queries: number[][]): number {
  const MAX = 10 ** 9 + 7;

  const prefixSum = Array(nums.length).fill(0);
  prefixSum[0] = moduloBy(nums[0], MAX);
  for (let idx = 1; idx < nums.length; idx++) {
    prefixSum[idx] = moduloBy(prefixSum[idx - 1] + nums[idx], MAX);
  }

  let result = 0;
  for (const [l, r] of queries) {
    const querySum =
      l === 0 ? prefixSum[r] : moduloBy(prefixSum[r] - prefixSum[l - 1], MAX);
    result = moduloBy(result + querySum, MAX);
  }

  return result;
}
