type Position = [row: number, column: number];

function position(str: string): Position {
  const [_columnChar, _row] = str.split("");
  const column = 1 + (_columnChar.charCodeAt(0) - "a".charCodeAt(0));
  const row = parseInt(_row);
  return [row, column];
}

function moves(position: Position): Position[] {
  const forwardSize = 2;
  const sidewaysSize = 1;

  const directions = [
    [-forwardSize, +sidewaysSize],
    [-sidewaysSize, +forwardSize],
    [+sidewaysSize, +forwardSize],
    [+forwardSize, +sidewaysSize],
    [+forwardSize, -sidewaysSize],
    [+sidewaysSize, -forwardSize],
    [-sidewaysSize, -forwardSize],
    [-forwardSize, -sidewaysSize],
  ];

  const [currentRow, currentColumn] = position;

  let positions: Position[] = [];
  for (let [rowDirection, columnDirection] of directions) {
    const newRow = currentRow + rowDirection;
    const newColumn = currentColumn + columnDirection;
    // We are not zero-indexed so the range for rows and columns is between 1 and 8.
    if (newRow >= 1 && newRow <= 8 && newColumn >= 1 && newColumn <= 8) {
      positions.push([newRow, newColumn]);
    }
  }

  return positions;
}

function solution(cell: string): number {
  const knight = position(cell);

  const numberOfMoves = moves(knight).length;

  return numberOfMoves;
}
