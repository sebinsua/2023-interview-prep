function solution(inputArray: number[]): number {
  let totalIncrements = 0;

  let previous = inputArray[0];
  for (let idx = 1; idx < inputArray.length; idx++) {
    if (previous >= inputArray[idx]) {
      const incrementsRequired = previous - inputArray[idx] + 1;

      totalIncrements += incrementsRequired;
      inputArray[idx] += incrementsRequired;
    }
    previous = inputArray[idx];
  }

  return totalIncrements;
}
