function position(str: string): [row: number, column: number] {
  const [_columnChar, _row] = str.split("");
  const column = 1 + (_columnChar.charCodeAt(0) - "a".charCodeAt(0));
  const row = parseInt(_row);
  return [row, column];
}

function same(p1: [number, number], p2: [number, number]): boolean {
  const rowDiff = Math.abs(p1[0] - p2[0]);
  const columnDiff = Math.abs(p1[1] - p2[1]);

  return rowDiff === columnDiff;
}

function solution(bishop: string, pawn: string): boolean {
  const bishopPosition = position(bishop);
  const pawnPosition = position(pawn);

  console.log({ bishopPosition, pawnPosition });
  return same(bishopPosition, pawnPosition);
}
