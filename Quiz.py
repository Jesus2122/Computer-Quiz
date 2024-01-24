print("Welcome to my fun quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit": 
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is 200 + 400? ")
if answer == "600": 
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory": 
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is 4! ? ")
if answer == "24": 
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")
