#총 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다.
#2차원 배열 만들기
a=[input() for i in range(5)]

max_len = max(len(row) for row in a)

# 세로줄만 출력하기
# j가 행, i가 열
for i in range(max_len): # 행은 가장 긴 문자열의 길이
  for j in range(5): # 열은 무조건 5개
    if i<len(a[j]): #인덱스 관리 ->  열이 3개인지, 4개인지
        # i <= len(a[j])이면 안되는 이유
        # i는 인덱스 len은 길이잖아
        # 길이가 4라고 하면
        # 0 < 4 , 1 < 4, 2 < 4, 3 < 4 이미 인덱스 끝남.. 같아지면 안돼
      print(a[j][i], end="") # 인덱스 조건을 만족할 때만 출력하기


