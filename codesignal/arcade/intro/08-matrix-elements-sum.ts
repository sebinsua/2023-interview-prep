function solution(matrix: number[][]): number {
  const rows = matrix.length;
  const columns = matrix[0].length;

  let cost = 0;
  for (let column = 0; column < columns; column++) {
    for (let row = 0; row < rows; row++) {
      if (matrix[row][column] === 0) {
        break;
      }
      cost += matrix[row][column];
    }
  }

  return cost;
}
