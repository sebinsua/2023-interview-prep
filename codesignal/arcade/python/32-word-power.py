def solution(word):
    num = {char: index + 1 for index, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
    return sum([num[ch] for ch in word])
