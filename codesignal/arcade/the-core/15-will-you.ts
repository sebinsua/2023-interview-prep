function solution(young: boolean, beautiful: boolean, loved: boolean): boolean {
  if (young && beautiful && loved) {
    return false;
  }
  if (
    (!young && !beautiful && !loved) ||
    (!young && beautiful && !loved) ||
    (young && !beautiful && !loved)
  ) {
    return false;
  }

  return true;
}
