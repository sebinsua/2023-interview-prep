def solution(bestStudents, scholarships, allStudents):
    return all(bool(bestStudent in scholarships) for bestStudent in bestStudents) and set(scholarships) < set(allStudents)
