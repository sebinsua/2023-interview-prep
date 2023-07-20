import base64

def solution(encoding, message):
    return base64.b64decode(message, altchars=encoding).decode('utf-8')
