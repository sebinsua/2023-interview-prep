type Square = [[number, number], [number, number]];

function* squares(matrix: number[][]): Generator<Square> {
  for (let row = 0; row < matrix.length - 1; row++) {
    for (let column = 0; column < matrix[0].length - 1; column++) {
      const square: Square = [
        [matrix[row][column], matrix[row][column + 1]],
        [matrix[row + 1][column], matrix[row + 1][column + 1]],
      ];
      yield square;
    }
  }
}

function hash(matrix: number[][]) {
  return `${matrix[0].join(" ")}\n${matrix[1].join(" ")}`;
}

function solution(matrix: number[][]): number {
  const uniqueSquares = new Set<string>();
  for (let square of squares(matrix)) {
    uniqueSquares.add(hash(square));
  }

  return uniqueSquares.size;
}
