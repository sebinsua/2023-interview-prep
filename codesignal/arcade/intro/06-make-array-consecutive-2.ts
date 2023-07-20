function solution(statues: number[]): number {
  // Basically, we want to know the minimum and maximum
  // and we then want to know, conceivably, how many gaps
  // there are between them.
  //
  // I'm going to assume from the wording, that we only need
  // to add statues and that no statues need to be removed
  // (e.g. they are each unique).

  const min = Math.min(...statues);
  const max = Math.max(...statues);
  const statuesMap = new Map(statues.map((statue) => [statue, true]));

  let count = 0;
  for (let i = min; i < max; i++) {
    if (!statuesMap.has(i)) {
      count++;
    }
  }

  return count;
}
