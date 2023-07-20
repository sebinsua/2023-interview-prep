function solution(
  inputArray: number[],
  elemToReplace: number,
  substitutionElem: number
): number[] {
  return inputArray.map((value) =>
    value === elemToReplace ? substitutionElem : value
  );
}
