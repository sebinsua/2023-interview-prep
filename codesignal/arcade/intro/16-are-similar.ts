function solution(a: number[], b: number[]): boolean {
  if (a.length !== b.length) {
    return false;
  }

  let swapCandidateFromA;
  let swapCandidateFromB;
  let hasSwapped = false;
  for (let idx = 0; idx < a.length; idx++) {
    const aEl = a[idx];
    const bEl = b[idx];
    if (aEl !== bEl) {
      if (swapCandidateFromA === bEl) {
        hasSwapped = true;
        swapCandidateFromA = undefined;
        if (swapCandidateFromB === aEl) {
          swapCandidateFromB = undefined;
        }
      } else {
        if (hasSwapped) {
          return false;
        }

        swapCandidateFromA = aEl;
        swapCandidateFromB = bEl;
        continue;
      }
    }

    if (swapCandidateFromB === bEl) {
      swapCandidateFromB = undefined;
    }
  }

  if (swapCandidateFromA !== undefined) {
    return false;
  }

  if (swapCandidateFromB !== undefined) {
    return false;
  }

  return true;
}
