function solution(n: number): number {
  const hours = Math.floor(n / 60);
  const minutes = n % 60;
  return `${hours}${minutes}`
    .split("")
    .map((char) => parseInt(char))
    .reduce((acc, digit) => acc + digit, 0);
}
