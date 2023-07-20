function solution(inputArray: string[]): string[] {
  let longestStringLength = 0;
  let longestStrings: string[] = [];

  for (const string of inputArray) {
    if (string.length > longestStringLength) {
      longestStrings = [string];
      longestStringLength = string.length;
    } else if (string.length === longestStringLength) {
      longestStrings.push(string);
    }
  }

  return longestStrings;
}
