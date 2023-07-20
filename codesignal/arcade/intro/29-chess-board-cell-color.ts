function cellColor(cell: string) {
  const chars = cell.split("");

  // We convert the character-based index into a one-indexed numeric value.
  // We also ensure that a string digit is also a one-indexed numeric value.
  const x = (chars[0].charCodeAt(0) % "A".charCodeAt(0)) + 1;
  const y = parseInt(chars[1]);

  // We use a boolean true/false value to represent whether they are black or
  // white. We don't really care about the color persay, but deterministically
  // assign true when both coordinates are odd or even.
  return (x % 2 === 0) === (y % 2 === 0);
}

function solution(cell1: string, cell2: string): boolean {
  return cellColor(cell1) === cellColor(cell2);
}
