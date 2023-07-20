def solution(participants):
    return [
        game
        for game, participant in enumerate(participants)
        if participant < game
    ]
