def solution(ids, k):
    digitSum = lambda questionId: sum(int(d) for d in list(str(questionId)))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
