function solution(names: string[]): string[] {
  const newNames: string[] = [];

  const counter = new Map<string, number>();
  for (let name of names) {
    if (!counter.has(name)) {
      // We set 0 to show we've seen this name before.
      counter.set(name, 0);
      newNames.push(name);

      continue;
    }

    let count = counter.get(name)!;
    let newName = `${name}(${count + 1})`;
    while (counter.has(newName)) {
      count++;
      newName = `${name}(${count + 1})`;
    }
    counter.set(newName, 0);
    counter.set(name, count);

    newNames.push(newName);
  }

  return newNames;
}
