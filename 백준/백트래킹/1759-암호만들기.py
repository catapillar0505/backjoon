#반복횟수: 1

import sys

# 암호의 길이(L)와 사용할 수 있는 알파벳 개수(C)를 입력받아요
# 예: 4 6 → 4글자 암호를 만들건데, 6개 알파벳 중에서 골라요
L, C = map(int, input().split())

# 사용할 알파벳들을 입력받고 정렬해요 (사전순으로!)
# 예: a t c i s w → 정렬하면 → a c i s t w
letters = sorted(input().split())

# 모음은 a, e, i, o, u 이 5개예요! (모음 주머니 만들기)
vowels = set('aeiou')

# 암호를 만드는 함수예요 (백트래킹이라는 방법)
def backtrack(start, password):
    # start: 지금부터 몇 번째 알파벳부터 볼건지
    # password: 지금까지 만든 암호 (리스트로 저장)
    
    # 🎯 암호가 L개 글자가 되었나요? (완성!)
    if len(password) == L:
        
        # 모음이 몇 개인지 세어봐요
        # password에 있는 각 글자(c)가 모음인지 확인하고 개수를 세요
        vowel_count = sum(1 for c in password if c in vowels)
        
        # 자음 개수 = 전체 개수 - 모음 개수
        consonant_count = L - vowel_count
        
        # 📝 규칙 확인: 모음 1개 이상? 자음 2개 이상?
        if vowel_count >= 1 and consonant_count >= 2:
            # 규칙을 만족하면 암호 출력! (리스트를 문자열로 합쳐요)
            print(''.join(password))
        
        # 이 경우는 끝! 돌아가요 (더 이상 글자 추가 안 함)
        return
    
    # 🔄 아직 L개가 안 됐으면, 더 골라야 해요!
    # start번째부터 마지막(C-1)번째 알파벳까지 하나씩 살펴봐요
    for i in range(start, C):
        # i번째 알파벳을 암호에 추가해요! 
        # 예: password가 ['a']이고 letters[i]가 'c'면 → ['a', 'c']
        password.append(letters[i])
        
        # 🎯 재귀 호출: "방금 i번째를 골랐으니, 이제 i+1번째부터 또 골라봐!"
        # 예: 'a'를 골랐으면, 다음엔 'a' 다음 알파벳들 중에서 골라요
        backtrack(i + 1, password)  
        
        # ⬅️ 백트래킹: 방금 넣은 글자를 다시 빼요 (다른 경우도 시도해보기 위해)
        # 예: ['a', 'c']에서 'c'를 빼서 다시 ['a']로 만들어요
        password.pop()

# 🚀 시작! 0번째부터, 빈 암호([])로 시작해요
backtrack(0, [])