type TupleSequence<T, L, A extends [...any]> = A["length"] extends L
  ? A
  : TupleSequence<T, L, [...A, T]>;
type Tuple<T, L> = TupleSequence<T, L, []>;

function* squares<Size extends number>(
  size: Size,
  image: number[][]
): Generator<Tuple<Tuple<number, Size>, Size>> {
  const rows = image.length;
  const columns = image[0].length;
  for (let i = 0; i <= rows - size; i += 1) {
    for (let j = 0; j <= columns - size; j += 1) {
      let square = [];
      for (let newRow = 0; newRow < size; newRow++) {
        square.push(image[i + newRow].slice(j, j + size));
      }
      yield square as Tuple<Tuple<number, Size>, Size>;
    }
  }
}

function average(image: number[][]) {
  const rows = image.length;
  const columns = image[0].length;

  const sum = image.reduce(
    (acc1, value1) => acc1 + value1.reduce((acc2, value2) => acc2 + value2, 0),
    0
  );

  return Math.floor(sum / (rows * columns));
}

function chunk<T>(size: number, values: T[]): T[][] {
  return Array.from({ length: Math.ceil(values.length / size) }, (v, i) =>
    values.slice(i * size, i * size + size)
  );
}

function solution(image: number[][]): number[][] {
  const BLUR_SQUARE_SIZE = 3;

  const blurredValues = Array.from(squares(BLUR_SQUARE_SIZE, image)).map(
    average
  );

  const NEW_SQUARE_SIZE = image[0].length - BLUR_SQUARE_SIZE + 1;

  return chunk(NEW_SQUARE_SIZE, blurredValues);
}
