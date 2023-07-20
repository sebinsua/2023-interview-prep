function solution(inputString: string): string {
  const match = inputString.match(/(\d)/);
  if (!match || match.length !== 2) {
    throw new Error(
      "The problem description shouldn't have allowed this to happen."
    );
  }

  const [, digit] = match;

  return digit;
}
