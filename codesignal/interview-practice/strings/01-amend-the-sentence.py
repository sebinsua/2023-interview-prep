def solution(s: str):
    sentence = ""
    for char in s:
        if char.isupper():
            sentence += f" {char.lower()}" if len(sentence) != 0 else char.lower()
        else:
            sentence += char

    return sentence
