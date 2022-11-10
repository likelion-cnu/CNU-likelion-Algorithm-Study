def solution(progresses, speeds):
    answer = []
    r = 0

    progresses = [i+j for i, j in zip(progresses, speeds)]
    while len(progresses) > 0:
        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            r += 1
        else:
            if r > 0:
                answer.append(r)
                r = 0
            progresses = [i+j for i, j in zip(progresses, speeds)]

    answer.append(r)
    return answer

# 100점!