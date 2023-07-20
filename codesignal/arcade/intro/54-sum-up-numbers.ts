const DIGITS = new Set("0123456789");

function solution(inputString: string): number {
  let count = 0;

  let numericStrings = [""];
  for (let char of inputString) {
    if (!DIGITS.has(char)) {
      if (numericStrings[numericStrings.length - 1].length > 0) {
        count += parseInt(numericStrings[numericStrings.length - 1]);
        numericStrings.push("");
      }
      continue;
    }

    numericStrings[numericStrings.length - 1] += char;
  }

  if (numericStrings[numericStrings.length - 1].length > 0) {
    count += parseInt(numericStrings[numericStrings.length - 1]);
  }

  return count;
}
