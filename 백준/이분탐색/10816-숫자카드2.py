# -*- coding: utf-8 -*-

# ================================
# 문제 유형 분석 (예제 기준)
# ================================
# 백준 10816번: 숫자 카드 2
#
# 예제 입력:
#   10
#   6 3 2 10 10 10 -10 -10 7 3
#   8
#   10 9 -5 2 3 4 5 -10
#
# 입력 의미:
#   - N = 10 (상근이가 가진 카드 개수)
#   - 카드들: [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
#   - M = 8 (확인할 카드 개수)
#   - 확인할 카드들: [10, 9, -5, 2, 3, 4, 5, -10]
#
# 문제 목표:
#   각 확인할 카드가 상근이 카드에 몇 개 있는지 세기
#
# 예제 시뮬레이션 (lower_bound/upper_bound 방법):
#   정렬된 카드: [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
#                 인덱스: 0    1   2  3  4  5  6   7   8   9
#
#   10의 개수 세기:
#     lower_bound(10) = 7 (10이 처음 나타나는 위치)
#     upper_bound(10) = 10 (10보다 큰 수가 처음 나타나는 위치, 배열 끝)
#     개수 = 10 - 7 = 3개
#
#   9의 개수 세기:
#     lower_bound(9) = 7 (9 이상인 첫 위치는 10)
#     upper_bound(9) = 7 (9 초과인 첫 위치는 10)
#     개수 = 7 - 7 = 0개 (없음!)
#
#   3의 개수 세기:
#     lower_bound(3) = 3 (3이 처음 나타나는 위치)
#     upper_bound(3) = 5 (3보다 큰 수가 처음 나타나는 위치는 6)
#     개수 = 5 - 3 = 2개
#
# 예상 출력: 3 0 0 1 2 0 0 2
#
# 핵심 아이디어:
#   - 정렬된 배열에서 특정 값의 범위를 찾기
#   - lower_bound: target 이상인 첫 번째 위치
#   - upper_bound: target 초과인 첫 번째 위치
#   - 개수 = upper_bound - lower_bound
#
# 시간복잡도: O(N log N + M log N)
#   - 정렬: O(N log N)
#   - M번 이분 탐색 (각각 lower, upper): O(M * 2 * log N)

# ================================
# 코드 분석 (예제 데이터 추적)
# ================================

import sys
input = sys.stdin.readline
# sys.stdin.readline은 input()보다 빠름 (대량 입력 시)

# 1. 상근이가 가진 카드 개수 입력
n = int(input().strip())
# 예제: n = 10
# strip()은 끝의 공백과 줄바꿈 제거

# 2. 카드들을 입력받아 정렬
cards = sorted(map(int, input().split()))
# 예제: 입력: "6 3 2 10 10 10 -10 -10 7 3"
#       map(int, input().split()): [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
#       sorted(): [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
# cards = [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
# 인덱스:   0    1   2  3  4  5  6   7   8   9

# 3. 확인할 카드 개수 입력
m = int(input().strip())
# 예제: m = 8

# 4. 확인할 카드들 입력 (정렬하지 않음!)
his_cards = list(map(int, input().split()))
# 예제: his_cards = [10, 9, -5, 2, 3, 4, 5, -10]
# 출력 순서가 입력 순서와 같아야 하므로 정렬 안 함!

# 5. lower_bound 함수: target 이상이 처음 나오는 위치
def lower_bound(arr, target):
    # arr: 정렬된 배열
    # target: 찾고자 하는 값
    # 반환: target 이상인 첫 번째 인덱스

    start, end = 0, len(arr)
    # start: 탐색 범위의 시작 (0)
    # end: 탐색 범위의 끝 (배열 길이)
    # 예제: arr = [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10], target = 3
    #       start = 0, end = 10

    while start < end:
        # start와 end가 만날 때까지 반복

        mid = (start + end) // 2
        # 중간 인덱스 계산

        if arr[mid] >= target:
            # arr[mid]가 target 이상이면
            # target이 왼쪽 절반에 있을 수 있음
            end = mid
            # end를 mid로 이동 (mid 포함)

        else:  # arr[mid] < target
            # arr[mid]가 target보다 작으면
            # target은 오른쪽 절반에 있음
            start = mid + 1
            # start를 mid+1로 이동 (mid 제외)

    # start == end가 되면 종료
    # start가 target 이상인 첫 번째 위치
    return start

# 예제에서 lower_bound(cards, 3) 추적:
#   cards = [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
#   target = 3
#
#   초기: start=0, end=10
#
#   1회전: mid=5, arr[5]=6 >= 3 -> end=5
#   2회전: start=0, end=5, mid=2, arr[2]=2 < 3 -> start=3
#   3회전: start=3, end=5, mid=4, arr[4]=3 >= 3 -> end=4
#   4회전: start=3, end=4, mid=3, arr[3]=3 >= 3 -> end=3
#
#   종료: start=3, end=3
#   return 3 (3이 처음 나타나는 위치)

# 6. upper_bound 함수: target 초과가 처음 나오는 위치
def upper_bound(arr, target):
    # arr: 정렬된 배열
    # target: 찾고자 하는 값
    # 반환: target 초과인 첫 번째 인덱스

    start, end = 0, len(arr)
    # 예제: arr = [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10], target = 3
    #       start = 0, end = 10

    while start < end:
        mid = (start + end) // 2

        if arr[mid] > target:
            # arr[mid]가 target 초과이면
            # target보다 큰 값이 왼쪽에도 있을 수 있음
            end = mid
            # end를 mid로 이동 (mid 포함)

        else:  # arr[mid] <= target
            # arr[mid]가 target 이하이면
            # target보다 큰 값은 오른쪽에 있음
            start = mid + 1
            # start를 mid+1로 이동 (mid 제외)

    # start == end가 되면 종료
    # start가 target 초과인 첫 번째 위치
    return start

# 예제에서 upper_bound(cards, 3) 추적:
#   cards = [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
#   target = 3
#
#   초기: start=0, end=10
#
#   1회전: mid=5, arr[5]=6 > 3 -> end=5
#   2회전: start=0, end=5, mid=2, arr[2]=2 <= 3 -> start=3
#   3회전: start=3, end=5, mid=4, arr[4]=3 <= 3 -> start=5
#
#   종료: start=5, end=5
#   return 5 (3보다 큰 수가 처음 나타나는 위치, 즉 6의 위치)

# 7. 결과를 저장할 리스트
res = []

# 8. 각 확인할 카드에 대해 개수 계산
for c in his_cards:
    # c: 확인할 카드
    # 예제: c는 차례대로 10, 9, -5, 2, 3, 4, 5, -10

    # lower_bound와 upper_bound의 차이가 개수
    count = upper_bound(cards, c) - lower_bound(cards, c)

    # 문자열로 변환하여 결과에 추가
    res.append(str(count))

# 예제에서 각 카드의 개수 계산 과정:
#
# cards = [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
#
# c = 10:
#   lower_bound(cards, 10) = 7
#   upper_bound(cards, 10) = 10
#   개수 = 10 - 7 = 3
#   res = ['3']
#
# c = 9:
#   lower_bound(cards, 9) = 7 (9 이상인 첫 위치는 10)
#   upper_bound(cards, 9) = 7 (9 초과인 첫 위치는 10)
#   개수 = 7 - 7 = 0
#   res = ['3', '0']
#
# c = -5:
#   lower_bound(cards, -5) = 2 (-5 이상인 첫 위치는 2)
#   upper_bound(cards, -5) = 2 (-5 초과인 첫 위치는 2)
#   개수 = 2 - 2 = 0
#   res = ['3', '0', '0']
#
# c = 2:
#   lower_bound(cards, 2) = 2
#   upper_bound(cards, 2) = 3
#   개수 = 3 - 2 = 1
#   res = ['3', '0', '0', '1']
#
# c = 3:
#   lower_bound(cards, 3) = 3
#   upper_bound(cards, 3) = 5
#   개수 = 5 - 3 = 2
#   res = ['3', '0', '0', '1', '2']
#
# c = 4:
#   lower_bound(cards, 4) = 5 (4 이상인 첫 위치는 6)
#   upper_bound(cards, 4) = 5 (4 초과인 첫 위치는 6)
#   개수 = 5 - 5 = 0
#   res = ['3', '0', '0', '1', '2', '0']
#
# c = 5:
#   lower_bound(cards, 5) = 5 (5 이상인 첫 위치는 6)
#   upper_bound(cards, 5) = 5 (5 초과인 첫 위치는 6)
#   개수 = 5 - 5 = 0
#   res = ['3', '0', '0', '1', '2', '0', '0']
#
# c = -10:
#   lower_bound(cards, -10) = 0
#   upper_bound(cards, -10) = 2
#   개수 = 2 - 0 = 2
#   res = ['3', '0', '0', '1', '2', '0', '0', '2']

# 9. 결과 출력 (공백으로 구분)
print(' '.join(res))
# ' '.join(res)는 리스트의 문자열들을 공백으로 연결
# 예제: ['3', '0', '0', '1', '2', '0', '0', '2'] -> "3 0 0 1 2 0 0 2"

# ================================
# Q&A (예제 중심 질문)
# ================================

# Q1: lower_bound와 upper_bound의 차이는?
# A1: lower_bound(x): x 이상인 첫 번째 위치
#     upper_bound(x): x 초과인 첫 번째 위치
#     예제: cards = [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
#           lower_bound(3) = 3 (3이 처음 나타나는 곳)
#           upper_bound(3) = 5 (3보다 큰 6이 나타나는 곳)

# Q2: 왜 개수가 upper_bound - lower_bound인가요?
# A2: lower_bound는 값의 시작 위치, upper_bound는 값의 끝 다음 위치
#     따라서 그 차이가 개수입니다.
#     예제: cards = [... 3, 3, 6 ...]
#                      ^3  ^5
#           3의 개수 = 5 - 3 = 2개

# Q3: 예제에서 9가 0개인 이유는?
# A3: cards = [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
#     9는 배열에 없습니다.
#     lower_bound(9) = 7 (9 이상인 첫 위치는 10이 있는 곳)
#     upper_bound(9) = 7 (9 초과인 첫 위치도 10이 있는 곳)
#     두 값이 같으므로 개수 = 0

# Q4: 왜 end를 len(arr)로 초기화하나요?
# A4: end는 탐색 범위의 끝을 나타냅니다.
#     len(arr)로 설정하면 배열의 모든 범위를 커버할 수 있습니다.
#     또한 upper_bound가 배열 끝을 넘어설 수 있기 때문입니다.
#     예제: upper_bound(10) = 10 (배열 길이)

# Q5: arr[mid] >= target과 arr[mid] > target의 차이는?
# A5: lower_bound: arr[mid] >= target (이상)
#       -> target과 같은 값도 왼쪽에서 찾을 수 있음
#     upper_bound: arr[mid] > target (초과)
#       -> target과 같은 값은 오른쪽으로 넘어감
#     이 차이로 시작과 끝 위치를 정확히 찾습니다!

# Q6: 예제에서 10의 개수가 3개인 과정은?
# A6: cards = [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
#                                       ^7  ^8  ^9
#     lower_bound(10) = 7 (10이 처음 나타나는 위치)
#     upper_bound(10) = 10 (10보다 큰 수의 위치, 배열 끝)
#     개수 = 10 - 7 = 3

# Q7: 왜 start < end이고 start <= end가 아닌가요?
# A7: start < end를 사용하면 start == end일 때 종료됩니다.
#     이때 start가 정확히 찾고자 하는 위치가 됩니다.
#     start <= end를 사용하면 무한 루프 위험이 있습니다.

# Q8: 정렬이 왜 필요한가요?
# A8: lower_bound와 upper_bound는 정렬된 배열에서만 동작합니다.
#     정렬되어 있어야 이분 탐색으로 빠르게 위치를 찾을 수 있습니다.
#     예제: [6, 3, 2, 10, ...] -> [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]

# Q9: his_cards는 왜 정렬하지 않나요?
# A9: 출력 순서가 입력 순서와 같아야 하기 때문입니다.
#     예제: 입력: [10, 9, -5, 2, 3, 4, 5, -10]
#           출력: [3, 0, 0, 1, 2, 0, 0, 2] (같은 순서)
#     만약 정렬하면 순서가 바뀌어 틀립니다!

# Q10: 시간복잡도는 어떻게 되나요?
# A10: 1) 정렬: O(N log N)
#      2) M번 이분 탐색: O(M * 2 * log N)
#         - 각 카드마다 lower_bound, upper_bound 2번
#      총합: O(N log N + M log N)
#      예제: N=10, M=8이면 약 10*3 + 8*2*3 = 78번 연산

# Q11: 음수 카드도 처리 가능한가요?
# A11: 네! 정렬만 되어 있으면 음수도 똑같이 처리됩니다.
#      예제: -10이 2개 있음
#            lower_bound(-10) = 0
#            upper_bound(-10) = 2
#            개수 = 2 - 0 = 2

# Q12: 같은 값이 여러 개 있어도 정확한가요?
# A12: 네! lower_bound와 upper_bound는 정확히 범위를 찾습니다.
#      예제: 3이 2개 ([3, 3])
#            lower_bound(3) = 3 (첫 3의 위치)
#            upper_bound(3) = 5 (3 다음의 6 위치)
#            개수 = 5 - 3 = 2 (정확!)

# Q13: Python의 bisect 모듈을 사용해도 되나요?
# A13: 네! bisect_left와 bisect_right를 사용하면 더 간단합니다.
#      from bisect import bisect_left, bisect_right
#      count = bisect_right(cards, c) - bisect_left(cards, c)
#      하지만 직접 구현하면 원리를 더 잘 이해할 수 있습니다!

# Q14: 예제에서 -5의 개수가 0인 이유는?
# A14: cards = [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
#      -5는 배열에 없습니다.
#      lower_bound(-5) = 2 (-5 이상인 첫 위치는 2)
#      upper_bound(-5) = 2 (-5 초과인 첫 위치는 2)
#      두 값이 같으므로 개수 = 0

# Q15: 이 알고리즘의 핵심은?
# A15: 정렬된 배열에서 특정 값의 "범위"를 찾는 것입니다.
#      lower_bound: 범위의 시작
#      upper_bound: 범위의 끝 다음
#      차이: 개수
#      이분 탐색으로 빠르게 O(log N)에 찾을 수 있습니다!
