function solution(address: string): string {
  let atIndex = -1;
  for (let i = address.length - 1; i > 0; i--) {
    const char = address[i];
    if (char === "@") {
      atIndex = i;
      break;
    }
  }
  return address.slice(atIndex + 1);
}
