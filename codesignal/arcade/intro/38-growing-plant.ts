function solution(
  upSpeed: number,
  downSpeed: number,
  desiredHeight: number
): number {
  // This question isn't phrased well. When they say, "how many days it'll take for
  // the plant to reach this height", they meant literally how many days -- not
  // inclusive of the final night.

  // Therefore, if the `upSpeed` during the day is greater than than the `desiredHeight`
  // we can immediately return 1 day.
  if (upSpeed >= desiredHeight) {
    return 1;
  }

  // If you try to calculate how much the `upSpeed - downSpeed` difference
  // fits within `desiredHeight` you will get the wrong answer as what we
  // need to find out is `nDays * (upSpeed - downSpeed) + upSpeed = desiredHeight`
  // and we might end up with a larger number of days than required if `upSpeed`
  // was high but negated by a similarly high `downSpeed`.
  //
  // Solving the equation:
  //
  // desiredHeight = nDays * (upSpeed - downSpeed) + upSpeed
  // desiredHeight - upSpeed = nDays * (upSpeed - downSpeed)
  // (desiredHeight - upSpeed) / (upSpeed - downSpeed) = nDays
  //
  // But:
  // (1) We need whole numbers so have to `Math.ceil` to round up the number of days.
  // (2) This gives us the number of days up to `(desiredHeight - upSpeed)` so we must
  //     then add `1` to this to include the following daytime period of that day
  //     that we are including to get to the highest height before the nightime
  //     reduces the height of our plant again.
  return Math.ceil((desiredHeight - upSpeed) / (upSpeed - downSpeed)) + 1;
}
