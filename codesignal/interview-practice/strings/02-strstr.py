def solution_has_bad_worst_case(s, x):
    word_length = len(x)
    string_length = len(s)
    for i in range(string_length):
        if (i + word_length) > string_length:
            break

        if x[0] == s[i]:
            j = 0
            while j < word_length:
                if x[j] != s[i + j]:
                    break
                j += 1
            if j > word_length - 1:
                return i

    return -1


def solution_has_bad_worst_case_2(s, x):
    word_length = len(x)
    string_length = len(s)
    for i in range(string_length - word_length + 1):
        if s[i : i + word_length] == x:
            return i

    return -1


def build_failure_table(pattern):
    failure_table = [0] * len(pattern)
    i, j = 0, 1

    while j < len(pattern):
        if pattern[i] == pattern[j]:
            failure_table[j] = i + 1
            i += 1
            j += 1
        else:
            if i != 0:
                i = failure_table[i - 1]
            else:
                failure_table[j] = 0
                j += 1

    return failure_table


def kmp_search(text, pattern):
    if len(pattern) == 0:
        return 0

    failure_table = build_failure_table(pattern)
    i, j = 0, 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        else:
            if j != 0:
                j = failure_table[j - 1]
            else:
                i += 1

    return -1


def solution(s, x):
    return kmp_search(s, x)
