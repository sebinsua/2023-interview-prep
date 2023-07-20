function solution(
  min1: number,
  min2_10: number,
  min11: number,
  s: number
): number {
  if (min1 > s) {
    return 0;
  }

  let minutes = 1;
  s -= min1;

  for (let i = 2; i <= 10 && s >= min2_10; i++) {
    minutes++;
    s -= min2_10;
    if (s < min2_10 && i < 10) {
      // If we run out of money to pay for the `min2_10` period
      // before we've left the period, we cannot move into the
      // `min11` period that follows it, so have to bail from
      // the call.
      return minutes;
    }
  }

  while (s >= min11) {
    minutes++;
    s -= min11;
  }

  return minutes;
}
