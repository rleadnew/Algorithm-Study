def solution(board, moves):
    answer = 0
    finalList = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                finalList.append(board[i][move - 1])
                board[i][move - 1] = 0 # 뽑힌 인형 자리를 비웠다고 표시

                if len(finalList) > 1:
                    if finalList[-1] == finalList[-2]:
                        finalList.pop(-1)
                        finalList.pop(-1)
                        answer += 2
                break # 인형이 한 자리에서 2번, 3번, ... 계속 뽑히지 않게 하기 위해( 한 번의 무브에서 하나의 인형만 뽑히게)

    return answer

test1 = solution([[0,0,0,0,0],
                  [0,0,1,0,3],
                  [0,2,5,0,1],
                  [4,2,4,4,2],
                  [3,5,1,3,1]], [1,5,3,5,1,2,1,4])

print(test1)

