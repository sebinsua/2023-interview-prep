function solution(product: number): number {
  if (product === 0) {
    return 10;
  }

  if (product < 10) {
    return product;
  }

  // We are trying to find a number of n digits
  // that multiply together to equal `product`,
  // however, we need this number to be the smallest
  // possible number that can do this.
  //
  // What does small mean? Less than all other attempts
  // if bruteforcing? Or, if we start with the minimum
  // and slowing increment upwards the first which is found?
  //
  // How do we know a number is small:
  // (1) The fewer the digits the better.
  // (2) The left-most digits should be small.
  //
  // Thoughts:
  // (1) There's no reason to ever contain 1 since multiplying
  //     by this value has no effect on the product. Start at `2...`
  // (2) 22, 23, 24, 25, 26, 27, 28, 29, ...
  //     There is no difference between 23 and 32 other than 23 being
  //     a smaller number and therefore more optimal choice.
  // (3) It's cheaper to increment the right-most values first, and
  //     always better to increment than to add a digit. Consequentially
  //     we should start with the digit 9 first and then decrement this
  //     as it helps us to avoid extra digits.
  // (4) If the number is prime, we can't break it down into factors,
  //     and we have to return -1.
  // (5) Either way, all factors will need to be less than 9, otherwise
  //     we won't be able to represent them as digits.

  let workingProduct = product;
  let result: number[] = [];
  for (let i = 9; i >= 2 && workingProduct > 1; i--) {
    while (workingProduct % i === 0) {
      workingProduct = workingProduct / i;
      result.push(i);
    }
  }

  if (workingProduct != 1) {
    // The number is prime and larger than 9.
    return -1;
  }

  // Convert the array of digits to a number starting with smallest digit.
  return parseInt([...result].reverse().join(""));
}
