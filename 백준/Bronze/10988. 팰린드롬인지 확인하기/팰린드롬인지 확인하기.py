word = list(input())
result = 0
length = len(word)
for i in range(0,length//2+1):
    if word[i] == word[length-i-1]:
        result= 1
    else:
        result = 0
        break                 
print(result)