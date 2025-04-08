# 첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
n = input()
list(n)
# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
res=""
res=''.join(sorted(n,reverse=True))
print(res)