function solution(name: string): boolean {
  if (/^\d/.test(name)) {
    return false;
  }

  if (/^[a-zA-Z0-9_]+$/.test(name)) {
    return true;
  }

  return false;
}
