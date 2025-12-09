# -*- coding: utf-8 -*-
# ========================================
# 1. 문제 유형 분석
# ========================================
# 키워드: 정렬, 빈도수, 2차원 배열
# 문제 유형: 시뮬레이션 + 정렬 문제
#
# 직관적 접근법:
# - 배열의 각 행/열을 빈도수로 정렬하고 다시 배열에 넣기
# - R 연산: 행 정렬 (가로 방향)
# - C 연산: 열 정렬 (세로 방향)
# - 시간이 지날수록 배열이 커지거나 작아질 수 있음
#
# 핵심 포인트:
# 1. 빈도수 세기: Counter 사용
# 2. 정렬 기준: (빈도, 숫자) 순서로 오름차순
# 3. 0은 무시!
# 4. 결과를 (숫자, 빈도) 순서로 배열에 삽입
# 5. 행/열의 최대 길이에 맞춰 0으로 패딩
#
# 함정 주의:
# - 배열 인덱스는 1부터 시작! (r, c는 1-indexed)
# - 100초가 지나도 조건을 만족 못 하면 -1
# - 행/열 크기가 100을 넘으면 100까지만 사용
#
# ========================================
# 2. 코드 분석
# ========================================

from collections import Counter

# r, c, k 입력 (1-indexed)
r, c, k = map(int, input().split())

# 초기 3x3 배열 입력
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

def sort_by_frequency(arr):
    """
    하나의 행 또는 열을 빈도수 기준으로 정렬

    입력: [1, 2, 1, 3] 같은 1차원 리스트
    출력: [1, 2, 2, 1, 3, 1] (숫자, 빈도 순서)

    정렬 기준:
    1. 빈도수 오름차순
    2. 빈도가 같으면 숫자 오름차순
    """
    # 0을 제외하고 빈도수 계산
    # 예: [1, 2, 1, 0] 를 Counter({1: 2, 2: 1}) 로 변환
    counter = Counter([x for x in arr if x != 0])

    # 빈도수 기준으로 정렬
    # items(): [(숫자, 빈도), ...]
    # key=lambda x: (x[1], x[0]): (빈도, 숫자) 순으로 정렬
    # 예: [(1, 2), (2, 1), (3, 1)] 정렬후 [(2, 1), (3, 1), (1, 2)]
    sorted_items = sorted(counter.items(), key=lambda x: (x[1], x[0]))

    # (숫자, 빈도) 순서로 평탄화
    # 예: [(2, 1), (3, 1), (1, 2)] 를 [2, 1, 3, 1, 1, 2] 로 변환
    result = []
    for num, freq in sorted_items:
        result.append(num)    # 숫자 추가
        result.append(freq)   # 빈도 추가

    return result

def operation_R(A):
    """
    R 연산: 모든 행을 정렬
    """
    new_A = []
    max_len = 0  # 가장 긴 행의 길이

    # 각 행을 정렬
    for row in A:
        sorted_row = sort_by_frequency(row)
        new_A.append(sorted_row)
        max_len = max(max_len, len(sorted_row))

    # 100을 넘으면 100으로 제한
    max_len = min(max_len, 100)

    # 모든 행의 길이를 max_len으로 맞춤 (0으로 패딩)
    # 예: [[1, 2], [3, 4, 5]] 를 [[1, 2, 0], [3, 4, 5]] 로 변환
    for i in range(len(new_A)):
        # 길이가 부족하면 0 추가
        new_A[i] = new_A[i][:max_len] + [0] * (max_len - len(new_A[i]))

    return new_A

def operation_C(A):
    """
    C 연산: 모든 열을 정렬
    전치 후 R 연산 후 다시 전치
    """
    # 전치 (행과 열 바꾸기)
    # 예: [[1,2],[3,4]] 를 [[1,3],[2,4]] 로 변환
    rows = len(A)
    cols = len(A[0])
    transposed = []
    for j in range(cols):
        col = []
        for i in range(rows):
            col.append(A[i][j])
        transposed.append(col)

    # R 연산 수행
    sorted_transposed = operation_R(transposed)

    # 다시 전치해서 원래 형태로
    rows = len(sorted_transposed)
    cols = len(sorted_transposed[0])
    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(sorted_transposed[i][j])
        result.append(row)

    return result

# 시뮬레이션 시작
time = 0

while time <= 100:
    # 배열의 현재 크기 확인
    rows = len(A)
    cols = len(A[0]) if rows > 0 else 0

    # A[r-1][c-1]이 k인지 확인 (1-indexed 를 0-indexed 로 변환)
    # 범위를 벗어나지 않는지도 확인
    if r-1 < rows and c-1 < cols and A[r-1][c-1] == k:
        print(time)
        exit()

    # 시간 초과
    if time == 100:
        break

    # R 연산 또는 C 연산
    if rows >= cols:  # 행의 개수 >= 열의 개수
        A = operation_R(A)
    else:  # 행의 개수 < 열의 개수
        A = operation_C(A)

    time += 1

# 100초가 지나도 조건 만족 못 함
print(-1)

# ========================================
# 3. Q&A
# ========================================
# Q1: 전치(transpose)가 뭔가요?
# A: 행과 열을 바꾸는 것입니다.
#    예: [[1,2,3],     [[1,4],
#         [4,5,6]]  를  [2,5],
#                       [3,6]]  로 변환
#    C 연산은 열을 정렬하는데, 전치하면 열이 행이 되므로
#    R 연산을 적용할 수 있습니다!
#
# Q2: Counter를 왜 사용하나요?
# A: 각 숫자가 몇 번 나왔는지 세기 위해서입니다.
#    예: [1, 1, 2] 를 Counter({1: 2, 2: 1}) 로 변환
#    리스트로 직접 세는 것보다 훨씬 간편합니다.
#
# Q3: lambda x: (x[1], x[0])은 무슨 뜻인가요?
# A: 정렬 기준을 지정하는 람다 함수입니다.
#    x는 (숫자, 빈도) 튜플이고,
#    (x[1], x[0])는 (빈도, 숫자) 순서로 정렬하라는 의미입니다.
#    예: [(1,2), (2,1)] 을 (빈도, 숫자) = [(2,1,1), (1,2,2)]
#        로 정렬하면 [(2,1), (1,2)]
#
# Q4: 왜 0을 무시하나요?
# A: 문제 조건입니다. 빈도수를 셀 때 0은 제외해야 합니다.
#    0은 "빈 칸"의 의미이므로 카운트하지 않습니다.
#
# Q5: 100개 제한은 왜 필요한가요?
# A: 배열이 무한정 커지는 것을 방지하기 위한 문제 조건입니다.
#    메모리와 시간을 절약하기 위해 100까지만 사용합니다.
#
# Q6: 1-indexed는 무슨 뜻인가요?
# A: 인덱스가 0부터가 아닌 1부터 시작한다는 의미입니다.
#    문제에서 r=1, c=1은 배열의 [0][0]을 의미합니다.
#    따라서 A[r-1][c-1]로 접근해야 합니다.
#
# Q7: 시간 복잡도는?
# A: 최악의 경우 100초 동안 매번 100x100 배열을 정렬하므로
#    O(100 * 100 * 100 * log(100)) = O(10^7) 정도로
#    충분히 빠릅니다.
#
# ========================================
# 학습 포인트
# ========================================
# 1. 시뮬레이션: 조건에 따라 배열 변형
# 2. Counter로 빈도수 계산
# 3. 커스텀 정렬: lambda 함수 사용
# 4. 전치(transpose)로 C 연산을 R 연산으로 변환
# 5. 배열 패딩: 0으로 길이 맞추기
# 6. 1-indexed vs 0-indexed 주의
