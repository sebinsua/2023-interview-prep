function* rows(grid: number[][]): Generator<number[]> {
  for (let row of grid) {
    yield row;
  }
}

function* columns(grid: number[][]): Generator<number[]> {
  const columns = grid[0].length;
  for (let columnIndex = 0; columnIndex < columns; columnIndex++) {
    const column: number[] = [];
    for (let row of grid) {
      column.push(row[columnIndex]);
    }

    yield column;
  }
}

type BuildTuple<
  ElementType,
  Length extends number,
  Accumulator extends [...any]
> = Accumulator["length"] extends Length
  ? Accumulator
  : BuildTuple<ElementType, Length, [...Accumulator, ElementType]>;

type Tuple<ElementType, Length extends number> = BuildTuple<
  ElementType,
  Length,
  []
>;

function* squares<Size extends number>(
  size: Size,
  grid: number[][]
): Generator<Tuple<Tuple<number, Size>, Size>> {
  const rows = grid.length;
  const columns = grid[0].length;
  for (let i = 0; i <= rows - size; i += size) {
    for (let j = 0; j <= columns - size; j += size) {
      let square: number[][] = [];
      for (let newRow = 0; newRow < size; newRow++) {
        square.push(grid[i + newRow].slice(j, j + size));
      }
      yield square as Tuple<Tuple<number, Size>, Size>;
    }
  }
}

function isSudokuSequenceValid(sequence: number[]): boolean {
  const uniqueValues = new Set(sequence);
  if (uniqueValues.size !== sequence.length) {
    return false;
  }
  for (let i = 1; i <= 9; i++) {
    if (!uniqueValues.has(i)) {
      return false;
    }
  }

  return true;
}

function unnest(grid: number[][]): number[] {
  return grid.reduce((acc, row) => [...acc, ...row], []);
}

function solution(grid: number[][]): boolean {
  for (let row of rows(grid)) {
    if (!isSudokuSequenceValid(row)) {
      return false;
    }
  }

  for (let column of columns(grid)) {
    if (!isSudokuSequenceValid(column)) {
      return false;
    }
  }

  for (let square of squares(3, grid)) {
    if (!isSudokuSequenceValid(unnest(square))) {
      return false;
    }
  }

  return true;
}
