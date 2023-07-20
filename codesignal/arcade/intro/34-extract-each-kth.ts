function solution(inputArray: number[], k: number): number[] {
  const returnArray: number[] = [];
  for (let i = 0; i < inputArray.length; i++) {
    if ((i + 1) % k === 0) {
      continue;
    }
    returnArray.push(inputArray[i]);
  }
  return returnArray;
}
