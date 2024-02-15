stud_score = input().split()
for n in range(0,len(stud_score)):
    stud_score[n] = int(stud_score[n])
high = 0
for score in stud_score:
    if score > high:
        high = score
print(f"highest is {high}")