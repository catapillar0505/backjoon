# -*- coding: utf-8 -*-

# ========================================================
# lower_bound/upper_bound vs 일반 이분탐색 차이점
# ========================================================

# ========================================================
# 1. 10816번 (숫자 카드 2) - lower_bound/upper_bound 사용
# ========================================================

# 문제 유형: "개수 세기" 문제
# 목표: 정렬된 배열에서 특정 숫자가 "몇 개" 있는지 세기

# 예제:
# 카드: [1, 2, 2, 2, 3, 5, 5]
# 질문: 2가 몇 개 있나요? -> 3개
# 질문: 5가 몇 개 있나요? -> 2개

# 왜 lower_bound와 upper_bound를 나눠서 사용하나?
# -> 중복된 값의 "범위"를 찾아서 개수를 계산하기 위해!

# 시각화:
# arr = [1, 2, 2, 2, 3, 5, 5]
#        0  1  2  3  4  5  6  (인덱스)
#
# 2를 찾을 때:
#   lower_bound(2) = 1  (2가 처음 시작하는 위치)
#                  ^
#   upper_bound(2) = 4  (2보다 큰 수가 시작하는 위치)
#                      ^
#   개수 = 4 - 1 = 3개

# lower_bound: target "이상"인 첫 번째 위치
def lower_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:  # target 이상이면
            end = mid           # 왼쪽으로 (더 작은 인덱스 찾기)
        else:
            start = mid + 1
    return start

# upper_bound: target "초과"인 첫 번째 위치
def upper_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > target:   # target 초과면
            end = mid           # 왼쪽으로
        else:
            start = mid + 1
    return start

# 예제로 확인:
arr = [1, 2, 2, 2, 3, 5, 5]

print("10816번 방식 (개수 세기):")
print(f"배열: {arr}")
print(f"2의 lower_bound: {lower_bound(arr, 2)}")  # 1
print(f"2의 upper_bound: {upper_bound(arr, 2)}")  # 4
print(f"2의 개수: {upper_bound(arr, 2) - lower_bound(arr, 2)}")  # 3

print(f"5의 lower_bound: {lower_bound(arr, 5)}")  # 5
print(f"5의 upper_bound: {upper_bound(arr, 5)}")  # 7
print(f"5의 개수: {upper_bound(arr, 5) - lower_bound(arr, 5)}")  # 2

print(f"4의 lower_bound: {lower_bound(arr, 4)}")  # 4
print(f"4의 upper_bound: {upper_bound(arr, 4)}")  # 4
print(f"4의 개수: {upper_bound(arr, 4) - lower_bound(arr, 4)}")  # 0 (없음!)

# 핵심:
# - lower_bound와 upper_bound의 "차이"가 개수
# - 중복된 값의 범위를 찾는 것이 목적

print("\n" + "="*60 + "\n")

# ========================================================
# 2. 2512번 (예산) - 일반 이분탐색 사용
# ========================================================

# 문제 유형: "최적값 찾기" 문제
# 목표: 조건을 만족하는 "최대 상한액" 찾기

# 예제:
# 지역별 예산 요청: [120, 110, 140, 150]
# 총 예산: 485
# 질문: 모든 지역에 배정할 수 있는 최대 상한액은?

# 상한액이 127이면:
#   120 + 110 + 127 + 127 = 484 (485 이하, 가능!)
# 상한액이 128이면:
#   120 + 110 + 128 + 128 = 486 (485 초과, 불가능!)
# 답: 127

# 왜 하나의 이분탐색만 사용하나?
# -> "개수"를 세는게 아니라 "조건을 만족하는 최대값"을 찾는 것!

# 일반 이분탐색 (최적값 찾기)
def find_max_budget(budgets, total_budget):
    start = 0
    end = max(budgets)  # 최대 예산 요청액
    result = 0

    while start <= end:
        mid = (start + end) // 2  # 상한액 후보

        # mid를 상한액으로 했을 때 총합 계산
        current_sum = 0
        for b in budgets:
            if b > mid:
                current_sum += mid  # 상한액 적용
            else:
                current_sum += b    # 요청액 그대로

        # 조건 확인
        if current_sum <= total_budget:
            # 가능하면 더 큰 상한액 시도
            result = mid  # 현재 mid는 가능한 답
            start = mid + 1  # 더 큰 값 찾기
        else:
            # 불가능하면 더 작은 상한액 시도
            end = mid - 1

    return result

# 예제로 확인:
budgets = [120, 110, 140, 150]
total = 485

print("2512번 방식 (최적값 찾기):")
print(f"예산 요청: {budgets}")
print(f"총 예산: {total}")
print(f"최대 상한액: {find_max_budget(budgets, total)}")

# 탐색 과정 시각화:
print("\n탐색 과정:")
start = 0
end = 150
step = 1

while start <= end:
    mid = (start + end) // 2
    current_sum = sum(min(b, mid) for b in budgets)

    print(f"Step {step}: start={start}, end={end}, mid={mid}")
    print(f"  상한액 {mid}일 때 총합: {current_sum}")

    if current_sum <= total:
        print(f"  -> {current_sum} <= {total}, 가능! 더 큰 값 시도")
        start = mid + 1
    else:
        print(f"  -> {current_sum} > {total}, 불가능! 더 작은 값 시도")
        end = mid - 1

    step += 1
    if step > 10:  # 무한루프 방지
        break

print("\n" + "="*60 + "\n")

# ========================================================
# 핵심 차이점 정리
# ========================================================

print("핵심 차이점:")
print()
print("1. 10816번 (숫자 카드 2):")
print("   목적: 중복된 값의 '개수' 세기")
print("   방법: lower_bound + upper_bound")
print("   이유: 특정 값의 '범위'를 찾아야 함")
print("   예: [1,2,2,2,3]에서 2가 몇 개? -> upper(2) - lower(2) = 4-1 = 3개")
print()
print("2. 2512번 (예산):")
print("   목적: 조건을 만족하는 '최대값' 찾기")
print("   방법: 일반 이분탐색 (하나만)")
print("   이유: 범위가 아니라 '최적의 값' 하나를 찾는 것")
print("   예: 총 예산 485로 가능한 최대 상한액은? -> 127")
print()

# ========================================================
# 언제 어떤 방법을 사용하나?
# ========================================================

print("\n언제 어떤 방법을 사용할까?")
print()
print("lower_bound/upper_bound 사용:")
print("  - 정렬된 배열에서 특정 값의 '개수' 세기")
print("  - 특정 값이 '처음 나타나는 위치' 찾기")
print("  - 특정 값이 '마지막 나타나는 위치' 찾기")
print("  - 중복된 값의 '범위' 찾기")
print()
print("일반 이분탐색 사용:")
print("  - 조건을 만족하는 '최소값' 또는 '최대값' 찾기")
print("  - '답'이 될 수 있는 값의 범위에서 최적값 찾기")
print("  - 결정 문제 (Yes/No)를 최적화 문제로 풀기")
print()

# ========================================================
# 실전 예제 비교
# ========================================================

print("\n실전 예제 비교:")
print()
print("Q: [1, 2, 2, 2, 3, 5, 5]에서 2가 몇 개?")
print("   -> lower_bound/upper_bound 사용 (개수 세기)")
print("   -> upper_bound(2) - lower_bound(2) = 4 - 1 = 3개")
print()
print("Q: 예산 [120, 110, 140, 150], 총 485로 가능한 최대 상한액?")
print("   -> 일반 이분탐색 사용 (최적값 찾기)")
print("   -> start=0, end=150 범위에서 최대값 찾기 -> 127")
print()

# ========================================================
# 코드 비교
# ========================================================

print("\n코드 비교:")
print()
print("10816번 코드 구조:")
print("  for 각 쿼리:")
print("    lb = lower_bound(arr, query)")
print("    ub = upper_bound(arr, query)")
print("    개수 = ub - lb")
print()
print("2512번 코드 구조:")
print("  start, end = 최소값, 최대값")
print("  while start <= end:")
print("    mid = (start + end) // 2")
print("    if 조건만족(mid):")
print("      result = mid  # 답 갱신")
print("      start = mid + 1  # 더 큰 값 시도")
print("    else:")
print("      end = mid - 1  # 더 작은 값 시도")
print()

# ========================================================
# 마무리
# ========================================================

print("\n마무리:")
print("- 10816번: lower/upper bound는 '범위 찾기' 도구")
print("- 2512번: 일반 이분탐색은 '최적값 찾기' 도구")
print("- 같은 이분탐색이지만 '목적'이 다릅니다!")
