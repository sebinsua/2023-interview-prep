const ALPHABET = "abcdefghijklmnopqrstuvwxyz".split("");

function solution(inputString: string): boolean {
  const counter = new Map(ALPHABET.map((char) => [char, 0]));
  for (let char of inputString) {
    counter.set(char, counter.has(char) ? counter.get(char)! + 1 : 1);
  }

  let previous: number = Infinity;
  for (let alphabetChar of ALPHABET) {
    if (counter.get(alphabetChar)! > previous) {
      return false;
    }
    previous = counter.get(alphabetChar)!;
  }

  return true;
}
