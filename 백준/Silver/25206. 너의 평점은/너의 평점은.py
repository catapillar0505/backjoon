grade_list = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
grade_score = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
total_credit =0
total_score = 0
for i in range(20):
    n,c,g = input().split()
    c = float(c)
    if g == 'P':
       continue
    total_credit += c
    idx = grade_list.index(g)
    total_score += (grade_score[idx]*c)

print(total_score/total_credit)