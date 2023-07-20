function oneApart(s1: string, s2: string) {
  if (s1.length !== s2.length) {
    return false;
  }

  let seenDifference = false;
  for (let charIndex = 0; charIndex < s1.length; charIndex++) {
    const c1 = s1[charIndex];
    const c2 = s2[charIndex];

    if (c1 !== c2) {
      if (seenDifference) {
        return false;
      }
      seenDifference = true;
    }
  }

  if (!seenDifference) {
    return false;
  }

  return true;
}

function solution(inputArray: string[]): boolean {
  if (inputArray.length === 0) {
    return true;
  }

  // Depth-first search
  function dfs(path: string[], remaining: string[]): boolean {
    // If there are no more elements a `path` has been found that is valid.
    if (remaining.length === 0) {
      return true;
    }

    // Otherwise, we get the `previousSequence` that was checked and appended to the `path`,
    const previousSequence = path[path.length - 1];
    for (let i = 0; i < remaining.length; i++) {
      // and test that the following sequence in the `remaining` list is one apart.
      // If it's not, we check the next element within the `remaining` list.
      if (!oneApart(previousSequence, remaining[i])) {
        continue;
      }

      // But if it's 'one apart', we continue our DFS from this point appending the valid element
      // onto our `path` and passing through every other element in a separate `remaining` list.
      if (
        dfs(
          [...path, remaining[i]],
          [...remaining.slice(0, i), ...remaining.slice(i + 1)]
        )
      ) {
        // This happens if all elements in the `path` are valid, and `remaining` is an empty list.
        return true;
      }
    }

    return false;
  }

  // For each element, build a `path` with it at the start, and every other element in a separate `remaining` list.
  for (let i = 0; i < inputArray.length; i++) {
    if (
      dfs(
        [inputArray[i]],
        [...inputArray.slice(0, i), ...inputArray.slice(i + 1)]
      )
    ) {
      // This happens if we find at least one valid `path` created by using each element
      // in `inputArray` as a prefix to the beginning of each path and doing a DFS on each
      // of these.
      return true;
    }
  }

  return false;
}
