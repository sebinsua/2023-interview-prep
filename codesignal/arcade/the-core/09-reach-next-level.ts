function solution(
  experience: number,
  threshold: number,
  reward: number
): boolean {
  return experience + reward >= threshold;
}
