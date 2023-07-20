function sum(ns: number[]) {
  return ns.reduce((acc, v) => acc + v, 0);
}

function solution(n: number): boolean {
  const nStr = String(n);
  if (nStr.length % 2 !== 0) {
    return false;
  }

  const middlePoint = nStr.length / 2;

  const firstHalf = Array.from(nStr.slice(0, middlePoint)).map((char) =>
    parseInt(char)
  );
  const secondHalf = Array.from(nStr.slice(middlePoint)).map((char) =>
    parseInt(char)
  );

  return sum(firstHalf) === sum(secondHalf);
}
