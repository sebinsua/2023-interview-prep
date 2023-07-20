function solution(score1: number, score2: number): boolean {
  // We're testing whether we have a valid finishing score.
  if (score1 === 6 && score2 < 5) {
    return true;
  }
  if (score2 === 6 && score1 < 5) {
    return true;
  }

  if (score1 === 7 && score2 >= 5 && score2 < 7) {
    return true;
  }
  if (score2 === 7 && score1 >= 5 && score1 < 7) {
    return true;
  }

  return false;
}
