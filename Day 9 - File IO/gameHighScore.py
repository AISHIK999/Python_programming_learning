# Python program to set the current score of a player as high score if it beats the initial high score

def score():
    sc = int(input("Enter your current score:\n"))
    return sc


currentScore = score()
f = open("highScore.txt")
highScore = int(f.read())
f.close()

if(currentScore > highScore):
    print("Congratulations! You just set a new high score!")
    f = open("highScore.txt", "w")
    f.write(str(currentScore))
    f.close
else:
    print("Oops! You were not able to break the previous high score! Better luck next time")
