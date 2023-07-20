import json

def solution(jsonFile):
    # Given a jsonFile we should do a BFS recursion through this while 
    # replacing the values of numbers with 0, strings with "" and lists
    # with []. 
    def replace(tree):
        output = dict()
        for (key, value) in tree.items():
            if isinstance(value, int) or isinstance(value, float):
                output[key] = 0
            elif isinstance(value, str):
                output[key] = ""
            elif isinstance(value, list):
                output[key] = []
            else:
                output[key] = replace(value)
        return output
    
    return json.dumps(replace(json.loads(jsonFile)))