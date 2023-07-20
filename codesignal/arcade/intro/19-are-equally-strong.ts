function solution(
  yourLeft: number,
  yourRight: number,
  friendsLeft: number,
  friendsRight: number
): boolean {
  // Basically, your strongest arm should match their strongest arm, no matter which arms
  // you are comparing, and your weakest arm should match their weakest arm, no matter
  // which arms these were.
  return (
    Math.max(yourLeft, yourRight) === Math.max(friendsLeft, friendsRight) &&
    Math.min(yourLeft, yourRight) === Math.min(friendsLeft, friendsRight)
  );
}
