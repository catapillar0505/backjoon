#총 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다.
#2차원 배열 만들기
a=[input() for i in range(5)]

max_len = max(len(row) for row in a)

# 세로줄만 출력하기
# j가 행, i가 열
for i in range(max_len):
  for j in range(5):
    if i<len(a[j]): #인덱스 관리 ->  열이 3개인지, 4개인지
      print(a[j][i], end="") # 인덱스 조건을 만족할 때만 출력하기


