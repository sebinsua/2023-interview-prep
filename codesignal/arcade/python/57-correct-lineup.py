def solution(athletes):
    return sum(
        ([athletes[(2*n)+1], athletes[2*n]] for n in range(len(athletes) // 2)),
        []
    )
