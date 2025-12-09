# 목표: 길이가 m인 모든 수열을 출력
# 방법: 현재까지 선택한 숫자들을 **리스트(stack)**에 저장
# 반복횟수: 10

import sys
input = sys.stdin.readline
output = sys.stdout.write

n,m=map(int,input().split())
stack=[]

def dfs(depth):
    if depth==m:
        output(" ".join(map(str,stack)) + "\n")
        return
    for i in range(1, n+1):
        stack.append(i)
        dfs(depth+1)
        stack.pop()
dfs(0)