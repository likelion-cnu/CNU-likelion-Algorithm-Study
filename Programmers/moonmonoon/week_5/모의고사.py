def solution(answers):
    answer = []

    scores = []
    zigsins = [[1, 2, 3, 4, 5],
               [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for zigsin in zigsins:
        i = 0
        score = 0
        for a in answers:
            if a == zigsin[i % len(zigsin)]:
                score += 1
            i += 1
        scores.append(score)

    for i, s in enumerate(scores):
        if s == max(scores):
            answer.append(i + 1)

    return answer
