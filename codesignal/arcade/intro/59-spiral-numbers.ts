type Direction = "RIGHT" | "DOWN" | "LEFT" | "UP";

function solution(n: number): number[][] {
  const matrix = new Array(n)
    .fill(() => new Array(n).fill(-1))
    .map((createRow) => createRow());

  let direction: Direction = "RIGHT";
  let row = 0;
  let column = 0;
  let i = 1;
  while (i <= n ** 2) {
    matrix[row][column] = i;

    switch (direction) {
      case "RIGHT": {
        column++;
        if (column === n - 1 || matrix[row][column + 1] !== -1) {
          direction = "DOWN";
        }
        break;
      }
      case "DOWN": {
        row++;
        if (row === n - 1 || matrix[row + 1][column] !== -1) {
          direction = "LEFT";
        }
        break;
      }
      case "LEFT": {
        column--;
        if (column === 0 || matrix[row][column - 1] !== -1) {
          direction = "UP";
        }
        break;
      }
      case "UP": {
        row--;
        if (row === 0 || matrix[row - 1][column] !== -1) {
          direction = "RIGHT";
        }
        break;
      }
    }

    i++;
  }

  return matrix;
}
