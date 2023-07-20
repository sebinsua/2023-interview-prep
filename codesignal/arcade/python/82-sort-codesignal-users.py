def solution(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))

@functools.total_ordering
class CodeSignalUser:
    def __init__(self, name: str, id: str, xp: str):
        self.id = int(id)  
        self.name = name
        self.xp = int(xp)
    
    def __eq__(self, other):
        return (self.xp, self.id) == (other.xp, other.id)

    def __lt__(self, other):
        if self.xp < other.xp:
            return True
        if self.xp == other.xp and self.id > other.id:
            return True
        return False
        
    def __str__(self):
        return self.name
