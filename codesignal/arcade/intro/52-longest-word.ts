const ALPHABET = new Set(
  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
);

function solution(text: string): string {
  let word = "";
  let longestWord = "";
  for (let char of text) {
    if (!ALPHABET.has(char)) {
      if (word.length > 0 && word.length > longestWord.length) {
        longestWord = word;
      }
      word = "";
      continue;
    }

    word += char;
  }

  if (word.length > 0 && word.length > longestWord.length) {
    longestWord = word;
  }

  return longestWord;
}
