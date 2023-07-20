function solution(s: string): string {
  let previous = "";
  let count = 0;

  let solution = "";
  for (let char of s) {
    if (char === previous) {
      count++;
    } else {
      solution += count > 1 ? `${count}${previous}` : previous;
      count = 1;
    }
    previous = char;
  }

  solution += count > 1 ? `${count}${previous}` : previous;

  return solution;
}
