function* chunk(
  size: number,
  inputArray: number[]
): Generator<[number, number]> {
  for (let i = 0; i < inputArray.length - 1; i++) {
    yield [inputArray[i], inputArray[i + 1]];
  }
}

function solution(inputArray: number[]): number {
  let max = -Number.MAX_SAFE_INTEGER;
  for (let [a, b] of chunk(2, inputArray)) {
    console.log(a, b, a * b);
    max = Math.max(max, a * b);
  }
  return max;
}
