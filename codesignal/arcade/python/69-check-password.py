def solution(attempts, password):
    def check():
        while True:
            next_attempt = yield
            if next_attempt == password:
                yield password

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1
