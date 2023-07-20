function solution(inputString: string): boolean {
  return /^(([0-9A-F]{2})\-){5}([0-9A-F]{2}){1}$/.test(inputString);
}
