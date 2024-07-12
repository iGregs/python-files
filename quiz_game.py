print("Welcome to Quiz Game")

playing = input("Do you want to play? ")

if playing.lower() != ("yes") :
   quit(print("bye"))

print("Okay! Let's play :)")
score = 0

answer1 = input("What is GPU stand for? : ")
if answer1 == ("graphics processing unit") :
    print('Correct!') 
    score += 1
else : print ('Incorrect')

answer1 = input("What is PSU stand for? : ").lower()
if answer1 == ("power supply") :
    print('Correct!')
    score += 1
else : print ('Incorrect')

answer1 = input("What is CPU stand for? : ").lower()
if answer1 == ("central processing unit") :
    print('Correct!')
    score += 1
else : print ('Incorrect')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/ 3) * 100)+ "%.")