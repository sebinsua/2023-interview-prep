function solution(a: number[]): number[] {
  const sortedPeople = a
    .filter((height) => height !== -1)
    .sort((a, b) => b - a);

  const treeBooleans = a.map((height) => (height === -1 ? true : false));

  const sortedPeopleAmongstTrees = [];
  for (let isTree of treeBooleans) {
    sortedPeopleAmongstTrees.push(isTree ? -1 : sortedPeople.pop());
  }

  return sortedPeopleAmongstTrees;
}
