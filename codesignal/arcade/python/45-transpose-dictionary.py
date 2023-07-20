def solution(scriptByExtension):
    return [
        (extension, file_name)
        for (file_name, extension) in
        sorted(scriptByExtension.items(), key=lambda pair: pair[1])
    ]
