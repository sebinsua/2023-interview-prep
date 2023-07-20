function* validDirections(matrix: boolean[][], row: number, column: number) {
  const rows = matrix.length;
  const columns = matrix[0].length;

  const deltas = [
    [-1, 0], // top
    [-1, 1], // top-right
    [0, 1], // right
    [1, 1], // bottom-right
    [1, 0], // bottom
    [1, -1], // bottom-left
    [0, -1], // left
    [-1, -1], // top-left
  ];

  for (const [dx, dy] of deltas) {
    const newRow = row + dx;
    const newColumn = column + dy;

    const isValid =
      newRow >= 0 &&
      newRow < rows &&
      newColumn >= 0 &&
      newColumn < columns &&
      matrix[newRow][newColumn];

    yield isValid;
  }
}

function solution(matrix: boolean[][]): number[][] {
  const rows = matrix.length;
  const columns = matrix[0].length;

  const countMatrix = new Array(rows)
    .fill(() => new Array(columns).fill(0))
    .map((generateRow) => generateRow());

  for (let row = 0; row < rows; row++) {
    for (let column = 0; column < columns; column++) {
      const count = Array.from(validDirections(matrix, row, column)).filter(
        Boolean
      ).length;

      countMatrix[row][column] = count;
    }
  }

  return countMatrix;
}
