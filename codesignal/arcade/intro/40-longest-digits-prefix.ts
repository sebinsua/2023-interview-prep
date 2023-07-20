function solution(inputString: string): string {
  const match = inputString.match(/^(\d+)/);
  if (!match || match.length !== 2) {
    return "";
  }

  const [, digits] = match;

  return digits;
}
