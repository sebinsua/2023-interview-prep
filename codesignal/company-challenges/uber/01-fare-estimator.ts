function solution(
  ride_time: number,
  ride_distance: number,
  cost_per_minute: number[],
  cost_per_mile: number[]
): number[] {
  const results: number[] = [];

  for (let i = 0; i < cost_per_minute.length; i++) {
    results.push(
      cost_per_minute[i] * ride_time + cost_per_mile[i] * ride_distance
    );
  }

  return results;
}
