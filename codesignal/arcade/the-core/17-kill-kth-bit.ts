function solution(n, k) {
  return (n & (2 ** (k - 1))) === 0 ? n : n ^ (2 ** (k - 1));
}
