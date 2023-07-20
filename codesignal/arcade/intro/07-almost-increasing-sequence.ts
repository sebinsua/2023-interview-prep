type TupleSeq_<T, L, A extends [...any]> = A["length"] extends L
  ? A
  : TupleSeq_<T, L, [...A, T]>;
type TupleSeq<T, L> = TupleSeq_<T, L, []>;

function* chunk<T, Size extends number>(
  size: Size,
  sequence: T[]
): Generator<TupleSeq<T, Size>> {
  for (let i = 0; i <= sequence.length - size; i++) {
    yield sequence.slice(i, i + size) as TupleSeq<T, Size>;
  }
}

function solution(sequence: number[]): boolean {
  const removalsConsideringAdjacentElements = Array.from(
    chunk(2, sequence)
  ).filter(([previous, middle]) => previous >= middle).length;

  const removalsConsideringElementsOneApart = Array.from(
    chunk(3, sequence)
  ).filter(([previous, _, next]) => previous >= next).length;

  // When looking at a chunk of two elements, we have
  // an issue if the sequence has more than one instance
  // in which we would need to remove an element to
  // make the sequence strictly increasing.
  if (removalsConsideringAdjacentElements > 1) {
    return false;
  }

  // When examining a chunk of three elements, we have
  // an issue if the sequence has more than one instance
  // in which, considering the element following the one
  // we tested in the previous check, we would need to
  // remove an element to ensure the sequence becomes
  // strictly increasing.
  if (removalsConsideringElementsOneApart > 1) {
    return false;
  }

  // Either zero or one elements could be removed
  // to create a strictly increasing subsequence.
  return true;
}
