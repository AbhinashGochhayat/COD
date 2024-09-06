import random as rand
arr = ['ST3LiOS','IRONMAN_AG','D_DEVIL','ABHISHEK@04OP','STAR_LORD','BLASTERBD2']

TEAM_A = []
while(len(TEAM_A)!=3):
    p = rand.randint(0,5)
    if arr[p] not in TEAM_A:
        TEAM_A.append(arr[p])
      
print("TEAM_A:",TEAM_A)

TEAM_B = []
for i in arr:
    if i not in TEAM_A:
        TEAM_B.append(i)

print("TEAM_B:", TEAM_B)
https://wallpapercave.com/wp/Pzb3zCA.jpg