from itertools import combinations

def solution(players, k):
    return sorted(map(lambda players: sorted(players), combinations(players, k)))
