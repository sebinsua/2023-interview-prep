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

function solution(t: Tree<number>): number[] {
  if (!t) {
    return [];
  }

  const result: number[] = [];

  let queue = [t];
  while (queue.length) {
    const node = queue.shift()!;

    result.push(node.value);

    if (node.left) {
      queue.push(node.left);
    }
    if (node.right) {
      queue.push(node.right);
    }
  }

  return result;
}
