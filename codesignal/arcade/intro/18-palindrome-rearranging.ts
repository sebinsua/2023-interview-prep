function counter(inputString: string): Map<string, number> {
  const counts = new Map<string, number>();
  for (let char of inputString) {
    counts.set(char, counts.has(char) ? counts.get(char) + 1 : 1);
  }
  return counts;
}

function solution(inputString: string): boolean {
  const counts = counter(inputString);

  // Filter out all of the even numbers of characters.
  // If there are no odd counts left then we have a palindrome,
  // but if there is a singular odd count it will work if one
  // of the elements is the centred in the palindrome.
  //
  // We don't have to check that the whole sequence is odd
  // or even since it's implied from the value of `countOdd`.
  const countOdd = Array.from(counts.values()).filter(
    (count) => count % 2 !== 0
  ).length;

  return countOdd <= 1;
}
