'''
1. n by n
2. n^2명의 학생. 항상 비어있는 좌석으로 이동
3. 다음과 같은 규칙으로 자리 선정

격자를 벗어나지 않는 4방향으로 인접한 칸 중 앉아있는 좋아하는 친구의 수가 가장 많은 위치로 갑니다.

만약 1번 조건을 만족하는 칸의 위치가 여러 곳이라면, 그 중 인접한 칸 중 비어있는 칸의 수가 가장 많은 위치로 갑니다. 단 이때 격자를 벗어나는 칸은 비어있는 칸으로 간주하지 않습니다.

만약 2번 조건까지 동일한 위치가 여러 곳이라면, 그 중 행 번호가 가장 작은 위치로 갑니다.

만약 3번 조건까지 동일한 위치가 여러 곳이라면, 그 중 열 번호가 가장 작은 위치로 갑니다.

 4. 점수 계산은 0명: 0점, 1명: 1점, 2명: 10점, 3명: 100점, 4명: 1000점

n1, n2, n3, n4는 전부 다른 숫자
모두 1 이상 n^2 이하의 수
n0는 겹치지 않음
'''

n = int(input())
student_order = []
student_like = {}
grid = [[0 for _ in range(n+1)] for _ in range(n+1)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n**2):
    n0, n1, n2, n3, n4 = map(int,input().split())
    student_order.append(n0)
    student_like[n0] = set([n1, n2, n3, n4])

def in_range(x, y):                                                 # 범위 안에 있는지 체크. True or False 반환
    return 1<= x <= n and 1<= y <= n

def find_seat(student):                                             # 차례가 온 학생이 들어갈 자리를 찾는 함수, [x, y]를 반환
    max_like, cand_seat, empty_adjacent = 0, [], []
    for x in range(1, n+1):
        for y in range(1, n+1):
            if grid[x][y] != 0:                                     # 이미 그 자리에 누구 있으면 패쓰
                continue
            adjacent_like = 0
            empty = 0
            for k in range(4):                                      # 4방향으로 췍!
                nx = x + dx[k]
                ny = y + dy[k]
                if in_range(nx, ny):                                # 근처 자리에 좋아하는 친구가 있거나 공석
                    if grid[nx][ny] in student_like[student]:
                        adjacent_like += 1
                    elif grid[nx][ny] == 0:
                        empty += 1

            if adjacent_like > max_like:
                max_like = adjacent_like
                cand_seat = [[x, y]]
                empty_adjacent = [empty]
            elif adjacent_like == max_like:
                cand_seat.append([x, y])
                empty_adjacent.append(empty)

    if len(cand_seat) == 1:                                         # 1번 규칙
        return cand_seat[0]

    sorted_empty = sorted(empty_adjacent, reverse=True)
    if len(cand_seat) >= 2:
        if sorted_empty[0] != sorted_empty[1]:                          # 2번 규칙
            index = empty_adjacent.index(sorted_empty[0])
            return cand_seat[index]

    sorted_seat = sorted(cand_seat, key = lambda x: x[0])           # 3번 규칙, 여기서는 굳이 sorted 할 필요 없을것 같음.
    if sorted_seat[0][0] != sorted_seat[1][0]:
        return sorted_seat[0]

    sorted_seat = sorted(cand_seat, key = lambda x: x[1])           # 4번 규칙
    return sorted_seat[0]


def score(num_of_adjacent:int) -> int:                              # 점수 계산
    return int(10**(num_of_adjacent-1))

def calculate_score():                                              # 전체 점수 계산하는 함수
    total_score = 0
    for x in range(1, n+1):
        for y in range(1, n+1):
            adjacent_like = 0
            for k in range(4):                                      # 4방향으로 췍!
                nx = x + dx[k]
                ny = y + dy[k]
                if grid[x][y] == 0:                                 # 학생 없는 경우 점수 패스
                    continue
                if in_range(nx, ny) and grid[nx][ny] in student_like[grid[x][y]]:
                    adjacent_like += 1
            total_score += score(adjacent_like)
    return total_score



# 자리잡기 시작
# print(student_order)
# print(student_like)
# print(grid)
grid [2][2] = student_order[0]
order = 1

while order < n**2:
    # print(grid)
    student = student_order[order]
    x, y = find_seat(student)
    grid[x][y] = student


    order += 1

# print(grid)
answer = calculate_score()
print(answer)