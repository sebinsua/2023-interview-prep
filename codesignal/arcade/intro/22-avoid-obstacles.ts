function max(inputArray: number[]): number {
  const maxArguments = 65535;

  let maxValue = -Infinity;
  for (let i = 0; i < inputArray.length; i += maxArguments) {
    const slice = inputArray.slice(i, i + maxArguments);
    const maxInSlice = Math.max(...slice);
    if (maxInSlice > maxValue) {
      maxValue = maxInSlice;
    }
  }

  return maxValue;
}

function solution(inputArray: number[]): number {
  if (inputArray.length === 0) {
    return 1;
  }

  const obstacles = new Set(inputArray);
  const maxObstacle = max(inputArray);

  // We know that `n` cannot be `1` since that would
  // hit every single obstable. We could test `2` and
  // `3` and so on, but this is inefficient.
  let n = 2;
  while (n <= maxObstacle) {
    if (
      !obstacles.has(n) &&
      inputArray.every((num) => num < n || num % n !== 0)
    ) {
      return n;
    }
    n++;
  }

  return n;
}
