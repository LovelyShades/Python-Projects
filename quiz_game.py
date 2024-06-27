print("\nwelcome to my computer quiz!\n")

playing = input("Do you want to play?\nPlease type \"yes\" or \"no\"\n")

if playing.lower() != "yes":
    quit()

print("\nOkay! Let' play!╰(*°▽°*)╯\n")

correctCount = 0
wrongCount = 0

answer = input("1) What does CPU stand for? \n a) central processing unit\n b) legos\n c) candy\n")
if answer.lower() == "a":
    print("Correct!\n")
    correctCount += 1
else: 
    print("Wrong\n")
    wrongCount += 1
    
answer = input("2) What does GPU stand for?\n a) Lukie Pookie\n b) graphics processing unit\n c) good pony unit\n")
if answer.lower() == "b":
    print("Correct!\n")
    correctCount += 1
else: 
    print("Wrong\n")
    wrongCount += 1
    
answer = input("3) What does RAM stand for?\n a) lemons\n b) bananas\n c) random access memory\n")
if answer.lower() == "c":
    print("Correct!\n")
    correctCount += 1
else: 
    print("Wrong\n")
    wrongCount += 1
    
print("You got " + str(correctCount) + " correct and " + str(wrongCount) + " wrong!\n")