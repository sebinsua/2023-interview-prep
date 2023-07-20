function validPart(p: string) {
  if (p.length === 0 || (p[0] === "0" && p.length > 1)) {
    return false;
  }
  const n = parseInt(p);
  return n >= 0 && n <= 255;
}

function solution(inputString: string): boolean {
  const matches = inputString.match(/^(\d+)\.(\d+)\.(\d+)\.(\d+)$/);
  if (!matches) {
    return false;
  }
  const [, p1, p2, p3, p4] = matches;
  return [p1, p2, p3, p4].every(validPart);
}
