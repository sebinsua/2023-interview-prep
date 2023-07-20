type TupleSeq_<T, L, A extends [...any]> = A["length"] extends L
  ? A
  : TupleSeq_<T, L, [...A, T]>;
type TupleSeq<T, L> = TupleSeq_<T, L, []>;

function* chunk<T, Size extends number>(
  size: Size,
  sequence: T[],
  skip: number = 1
): Generator<TupleSeq<T, Size>> {
  for (let i = 0; i < sequence.length; i += skip) {
    yield sequence.slice(i, i + size) as TupleSeq<T, Size>;
  }
}

function solution(a: number[]): number[] {
  let teamOneWeight = 0;
  let teamTwoWeight = 0;
  for (let [teamOnePersonWeight, teamTwoPersonWeight = 0] of chunk(2, a, 2)) {
    teamOneWeight += teamOnePersonWeight;
    teamTwoWeight += teamTwoPersonWeight;
  }

  return [teamOneWeight, teamTwoWeight];
}
