def solution(N, stages):
    length = len(stages)
    answer = []

    for i in range(1, N+1):
        userNum = stages.count(i)

        if length == 0:
            failRate = 0
        else:
            failRate = userNum / length

        answer.append((i, failRate))
        length -= userNum

    answer = sorted(answer, key=lambda x: -x[1])

    answer = [i[0] for i in answer]

    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(4, [4,4,4,4,4]))
