from urllib.parse import urlparse, parse_qs
from itertools import takewhile

def solution(url1, url2):
    similarity = 0
    
    url_parts_1 = urlparse(url1)
    url_query_1 = parse_qs(url_parts_1.query)
    url_parts_2 = urlparse(url2)
    url_query_2 = parse_qs(url_parts_2.query)
    
    if url_parts_1.scheme == url_parts_2.scheme:
        similarity += 5
    
    if url_parts_1.hostname == url_parts_2.hostname:
        similarity += 10
    
    similarity += len(
        list(
            takewhile(
                lambda pair: pair[0] == pair[1],
                zip(
                    url_parts_1.path.split('/')[1:],
                    url_parts_2.path.split('/')[1:]
                )
            )
        )
    )
    
    similarity += sum(
        2 if key_1 in url_query_2 and url_query_1[key_1] == url_query_2[key_1]
        else 1 if key_1 in url_query_2
        else 0
        for key_1 in url_query_1.keys()
    )
    
    return similarity