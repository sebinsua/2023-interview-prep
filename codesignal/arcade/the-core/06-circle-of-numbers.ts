function solution(n: number, firstNumber: number): number {
  // Therefore:
  //
  // when n = 10
  // 0 -> 5
  // 1 -> 6
  // 2 -> 7
  // 3 -> 8
  // 4 -> 9
  // 5 -> 0
  // 6 -> 1
  // 7 -> 2
  // 8 -> 3
  // 9 -> 4
  //
  // I need to sanity check for a circle with 5 points,
  // as it might work differently when we have odd number of points.
  //
  // when n = 5
  // 0 -> 3
  // 1 -> 4
  // 2 -> 5
  // 3 -> 0
  // 4 -> 1
  // 5 -> 2
  //
  // Looking at this, it seems that a way of looking at this is to
  // imagine incremental rotations producing a shift in the sequence
  // that wraps around, where the rounded-up midpoint of the sequence
  // maps to-and-from zero.
  const midpoint = Math.round(n / 2);

  if (firstNumber === 0) {
    return midpoint;
  }
  if (firstNumber === midpoint) {
    return 0;
  }

  return (midpoint + firstNumber) % n;
}
