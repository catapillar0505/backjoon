# 문제 목표
# 뱀이 벽이나 자기 몸에 부딪혀 게임이 끝날 때까지 걸린 시간(초)을 구하기

# 게임 조건에 맞게 하나하나 구현

# 뱀은 매 초마다 이동
# 사과를 먹으면 몸 길이 증가
# 사과가 없으면 몸 길이 유지 (꼬리 이동)
# 벽이나 자기 몸에 부딪히면 게임 종료
# 특정 시간에 방향 전환 명령 수행

# while 게임_진행 시뮬레이션:
#     1. 시간 증가 (time += 1)
    
#     2. 머리를 다음 칸으로 이동
#        - 현재 방향으로 한 칸 전진
    
#     3. 종료 조건 체크
#        - 벽에 부딪힘? (보드 범위 초과)
#        - 몸에 부딪힘? (이동할 칸이 뱀)
#        → 종료 시 break
    
#     4. 이동 처리
#        - 사과 있음: 머리만 추가 (몸 늘어남)
#        - 사과 없음: 머리 추가 + 꼬리 제거 (몸 유지)
    
#     5. 방향 전환 체크
#        - 현재 시간에 명령이 있으면 방향 변경

from collections import deque

# 🎮 게임 보드 크기 입력받기
n = int(input())

# 🍎 사과 개수 입력받기  
k = int(input())

# 📋 게임 보드 만들기 (0: 빈칸, 1: 사과, 2: 뱀)
board = [[0] * n for _ in range(n)]

# 🍎 사과 위치 표시하기
for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1  # 문제는 1부터, 우리는 0부터 시작

# 🔄 방향 전환 정보 입력받기
l = int(input())
turns = {}  # 딕셔너리: {몇 초: 어느 방향}

for _ in range(l):
    x, c = input().split()  # x초 후에 c방향으로 회전
    turns[int(x)] = c

# 🧭 방향 설정 (시계방향 순서)
# → (오른쪽): dx=0, dy=1
# ↓ (아래):   dx=1, dy=0  
# ← (왼쪽):   dx=0, dy=-1
# ↑ (위):     dx=-1, dy=0
dx = [0, 1, 0, -1]  # 행 이동
dy = [1, 0, -1, 0]  # 열 이동

# 🐍 뱀 초기 상태
time = 0  # 현재 시간
direction = 0  # 처음엔 오른쪽 보고 있어요
snake = deque([(0, 0)])  # 뱀의 몸 (머리가 첫 번째)
board[0][0] = 2  # (0,0)에 뱀이 있다고 표시

# 🎮 게임 시작!
while True:
    time += 1  # 1초 지났어요
    
    # 1️⃣ 뱀의 머리를 다음 칸으로 이동
    head_x, head_y = snake[0]  # 현재 머리 위치
    new_x = head_x + dx[direction]  # 새로운 행
    new_y = head_y + dy[direction]  # 새로운 열
    
    # 2️⃣ 벽에 부딪혔나요? (보드 밖으로 나감)
    if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
        break  # 게임 끝! 😵
    
    # 3️⃣ 자기 몸에 부딪혔나요?
    if board[new_x][new_y] == 2:  # 2는 뱀 몸이에요
        break  # 게임 끝! 😵
    
    # 4️⃣ 사과가 있나요?
    if board[new_x][new_y] == 1:  # 1은 사과예요
        # 🍎 사과 먹음! 몸이 길어져요
        board[new_x][new_y] = 2  # 머리가 여기로 옴
        snake.appendleft((new_x, new_y))  # 머리 추가
        # 꼬리는 그대로! (몸이 길어짐)
    else:
        # 💨 사과 없음! 몸 길이 그대로
        board[new_x][new_y] = 2  # 머리가 여기로 옴
        snake.appendleft((new_x, new_y))  # 머리 추가
        tail_x, tail_y = snake.pop()  # 꼬리 제거
        board[tail_x][tail_y] = 0  # 꼬리 있던 곳 빈칸으로
    
    # 5️⃣ 이번 초에 방향 전환해야 하나요?
    if time in turns:
        if turns[time] == 'L':  # 왼쪽으로 90도 회전
            direction = (direction - 1) % 4
            # 예: 오른쪽(0) → 위(3)
        else:  # 'D' 오른쪽으로 90도 회전  
            direction = (direction + 1) % 4
            # 예: 오른쪽(0) → 아래(1)

# 💯 게임이 끝난 시간 출력!
print(time)


## 시각적 설명:
# ```
# 초기 상태 (3x3 보드, 사과 2개):
# [S] [ ] [A]    S: 뱀
# [ ] [A] [ ]    A: 사과
# [ ] [ ] [ ]    

# 1초 후: 오른쪽 이동
# [ ] [S] [A]    
# [ ] [A] [ ]    
# [ ] [ ] [ ]    

# 2초 후: 사과 먹음! (몸 길어짐)
# [ ] [S][S]    
# [ ] [A] [ ]    
# [ ] [ ] [ ]    

# 방향 전환:
# 현재: → (오른쪽)
# L 명령: ↑ (위)
# D 명령: ↓ (아래)