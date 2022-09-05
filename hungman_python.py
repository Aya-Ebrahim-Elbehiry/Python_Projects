import random

#fixed set of words
word_set =('course','devops', 'programing' , 'django', 'container' , 'python' , 'project' )
# to choose random word
check_word = random.choice(word_set)
# ------------------------

player_n = input("input your name : ")
print("good luck " , player_n)

#  -------------------------------------------------
# to count down number of trails
life = 7
# initialization of list to print the chosen word
word_sol =[]
for s in check_word:
    word_sol.append("_")
print(word_sol)
# -------------------------------------------

while True :

    char = input('guess just one char : ' )
    if char in check_word[:]:
        for i in check_word[:]:
            if i == char and word_sol[check_word.index(i)] == "_":
                print(end=i)
                word_sol[check_word.index(i)] = i
            else:
                print(end="_")

        print(word_sol)
        if "_" not in word_sol:
            print(f"congratulation you won : {player_n} ")
            break
    elif char not in check_word:
        print("sorry your guess is not true tray again : " )
        life -= 1
        if life == 0 :
            print('sorry you failed in our game ^^ ')
            break
        print(f"you have : {life } trails  ")

