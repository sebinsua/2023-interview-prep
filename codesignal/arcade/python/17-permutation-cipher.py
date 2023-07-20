def solution(password, key):
    table = str.maketrans(dict(pair for pair in zip("abcdefghijklmnopqrstuvwxyz", key)))
    return password.translate(table)
