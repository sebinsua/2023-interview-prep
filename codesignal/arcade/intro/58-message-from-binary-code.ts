type TupleSequence_<T, L, A extends [...any]> = A["length"] extends L
  ? A
  : TupleSequence_<T, L, [...A, T]>;
type TupleSequence<T, L> = TupleSequence_<T, L, []>;

type Binary<Size extends number> = TupleSequence<0 | 1, Size>;

function* chunk<Size extends number>(
  size: Size,
  code: string
): Generator<Binary<Size>> {
  const items = Array.from(code);
  for (let i = 0; i < items.length; i += size) {
    yield items
      .slice(i, i + size)
      .map((digit) => parseInt(digit)) as Binary<Size>;
  }
}

function integerFrom8BitBinary(binary: Binary<8>): number {
  let value = 0;
  for (let i = binary.length - 1; i > 0; i--) {
    let j = binary.length - 1 - i;
    value += 2 ** j * binary[i];
  }
  return value;
}

function solution(code: string): string {
  let text = "";
  for (const binary of chunk(8, code)) {
    text += String.fromCharCode(integerFrom8BitBinary(binary));
  }

  return text;
}
