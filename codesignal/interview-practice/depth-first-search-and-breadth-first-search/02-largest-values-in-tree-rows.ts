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

  let result: number[] = [];

  let queue = [t];
  while (queue.length) {
    const nodes = queue.splice(0, queue.length);

    const max = Math.max(...nodes.map((node) => node.value));
    result.push(max);

    queue.push(
      ...nodes
        // @ts-ignore This version of TypeScript doesn't support `.flatMap`. LOL.
        .flatMap((node) => [node.left, node.right])
        .filter((v): v is Tree<number> => v !== undefined)
    );
  }

  return result;
}
