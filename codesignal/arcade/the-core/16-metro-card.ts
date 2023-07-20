function solution(lastNumberOfDays: number): number[] {
  // The Gregorian calendar consists of the following 12 months:
  //
  // January - 31 days
  // February - 28 days in a common year and 29 days in leap years
  // March - 31 days
  // April - 30 days
  // May - 31 days
  // June - 30 days
  // July - 31 days
  // August - 31 days
  // September - 30 days
  // October - 31 days
  // November - 30 days
  // December - 31 days
  const numberOfDaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

  let previous = numberOfDaysInMonth[numberOfDaysInMonth.length - 1];
  const options: number[] = [];
  for (const numberOfDays of numberOfDaysInMonth) {
    if (lastNumberOfDays === numberOfDays) {
      options.push(previous);
    }
    previous = numberOfDays;
  }

  return Array.from(new Set(options)).sort();
}
