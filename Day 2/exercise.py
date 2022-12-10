games = open("input.txt", "r")
games = games.readlines()

games1 = []
# Assuming that you have loaded data into a lines variable. 
for line in games:
    games1.append(line.strip().split(' '))
print(games1)

def map(x):
   if x == 'A' or x == 'X': 
        return 'rock'
   if x == 'B' or x == 'Y': 
        return 'paper'
   if x == 'C' or x == 'Z': 
        return 'scissors'

def get_winning(p1):
    if p1 == 'scissors': 
        return 'rock'
    if p1 == 'paper': 
        return 'scissors'
    if p1 == 'rock': 
        return 'paper'

def points(p):
    if p == 'rock':
        return 1
    if p == 'paper':
        return 2
    if p == 'scissors':
        return 3

i = 0
score1 = 0
score2 = 0
while i < len(games1):
    if get_winning(map(games1[i][0]))==map(games1[i][1]):
        print('ganhei')
        score1 = score1 + 0 + points(map(games1[i][0]))
        score2 = score2 + 6 + points(map(games1[i][1]))
    elif map(games1[i][0])==map(games1[i][1]):
        print('empatei')
        score1 = score1 + 3 + points(map(games1[i][0]))
        score2 = score2 + 3 + points(map(games1[i][1]))
    else: 
        print('perdi')
        score1 = score1 + 6 + points(map(games1[i][0]))
        score2 = score2 + 0 + points(map(games1[i][1]))
    i =i+1
print(score1)
print(score2)


