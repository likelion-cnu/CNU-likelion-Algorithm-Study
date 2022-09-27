C = 0
N_score = []
avg = 0
sad_truth = []

C = int(input())

for c in range(C):
    N_score = list(map(int, input().split()))
    avg = sum(N_score[1:])/N_score[0]
    good_student = 0

    for n in N_score[1:]:
        if n > avg:
            good_student += 1
    sad_truth.append(good_student/N_score[0] * 100)

for s in sad_truth:
    print("{:.3f}%".format(s))