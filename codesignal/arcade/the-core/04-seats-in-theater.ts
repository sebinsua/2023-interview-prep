function solution(
  nCols: number,
  nRows: number,
  col: number,
  row: number
): number {
  return (nRows - row) * (nCols - col + 1);
}
