def solution(strings, patterns):
    if len(strings) != len(patterns):
        return False

    word_to_pattern = dict()
    pattern_to_word = dict()
    for i in range(len(strings)):
        word, pattern = strings[i], patterns[i]
        if word in word_to_pattern:
            if pattern != word_to_pattern[word]:
                return False
        if pattern in pattern_to_word:
            if word != pattern_to_word[pattern]:
                return False
        else:
            word_to_pattern[word] = pattern
            pattern_to_word[pattern] = word

    return True
