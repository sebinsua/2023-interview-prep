import xml.etree.ElementTree as ET

def parse(root, output = None):
    if output is None:
        output = {}

    if root.tag not in output:
        output[root.tag] = {
            'children': {},
            'attributes': set(root.attrib.keys())
        }
    else:
        output[root.tag]['attributes'] = set(root.attrib.keys()) | output[root.tag]['attributes']

    children = {}
    for child in root:
        children.update(parse(child, output=children))

    for (tag_key, tag_value) in children.items():
        if tag_key in output[root.tag]['children']:
            output[root.tag]['children'][tag_key]['children'].update(tag_value.get('children', {}))
            output[root.tag]['children'][tag_key]['attributes'].update(tag_value.get('attributes', {}))
        else:
            output[root.tag]['children'][tag_key] = tag_value

    return output
    
def format(tree, depth = 0):
    output = []
    for (key, value) in tree.items():
        output.append(f"{'--' * depth}{key}({', '.join(sorted(value['attributes']))})")
        output.extend(format(value['children'], depth + 1))

    return output

def solution(xml):
    root = ET.fromstring(xml)
    
    tree = parse(root)

    return format(tree)