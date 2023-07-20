class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        from collections import defaultdict, deque
        
        # Lowercase all names for case insensitive checks.
        names = [name.lower() for name in self.names] 

        letters = "abcdefghijklmnopqrstuvwxyz"
        FROM = defaultdict(list)
        TO = defaultdict(list)
        for letter in letters:
            for name in names:
                first_character, last_character = name[0], name[-1]
                if letter == last_character:
                    FROM[letter].append(name)
                if letter == first_character:
                    TO[letter].append(name)

        start, end = False, False
        for letter in letters:
            if len(FROM[letter]) + 1 == len(TO[letter]):
                # More than one start node is not permissible for a Eulerian Path.
                if start:
                    return False
                start = True
            elif len(FROM[letter]) == len(TO[letter]) + 1:
                # More than one end node is not permissible for a Eulerian Path.
                if end:
                    return False
                end = True
            elif len(FROM[letter]) != len(TO[letter]):
                # Nodes with differing number of incoming and outgoing edges cannot form a Eulerian Path.
                return False

        # Check for connected graph using breadth-first search.
        visited = {0}
        queue = deque([0])
        while queue:
            name = queue.popleft()
            for index, teammate in enumerate(names):
                if index in visited:
                    continue
                
                if (
                    names[name][0] == teammate[-1]
                    or names[name][-1] == teammate[0]
                ):
                    visited.add(index)
                    queue.append(index)

        # If all names are visited it's a valid path.
        return len(visited) == len(names)

def solution(team):
    return bool(Team(team))
