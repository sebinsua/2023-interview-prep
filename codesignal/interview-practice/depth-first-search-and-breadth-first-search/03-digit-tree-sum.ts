// Binary trees are already defined with this interface:
class Tree<T> {
  value: T;
  left: Tree<T> | null;
  right: Tree<T> | null;

  constructor(value: T) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function sumPaths(paths: Array<number[]>) {
  const createNumber = (path) => parseInt(path.join(""));
  return paths.reduce((acc, path) => acc + createNumber(path), 0);
}

function solution(t: Tree<number>): number {
  if (!t) {
    return 0;
  }

  let paths: number[][] = [];
  let queue: Array<[number[], Tree<number>]> = [[[], t]];
  while (queue.length) {
    const [path, t] = queue.pop()!;

    if (!t.left && !t.right) {
      paths.push([...path, t.value]);
    }

    if (t.left) {
      queue.push([[...path, t.value], t.left]);
    }
    if (t.right) {
      queue.push([[...path, t.value], t.right]);
    }
  }

  return sumPaths(paths);
}
