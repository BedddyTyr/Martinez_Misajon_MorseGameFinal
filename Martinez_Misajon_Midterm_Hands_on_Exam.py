import operator as op
import random

randOp = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv}
numbersList = range(1, 100)
score = 0

for x in range(5):
    # randomization
    val1 = random.choice(numbersList)
    val2 = random.choice(numbersList)

    op = random.choice(list(randOp.keys()))

    # gameLoop
    question = eval(input("what is the answer of " + str(val1) + str(op) + str(val2) + " ?\n"))
    correctAnswer = randOp[op](val1, val2)

    if question == correctAnswer:
        print(str(val1) + str(op) + str(val2) + " = " + str(question))
        print("You are Correct!")
        score += 1

    else:
        print(str(val1) + str(op) + str(val2) + " = " + str(question))
        print("You are Wrong!")
        print("the correct answer is: ", correctAnswer)

print("You got ", score, " out of 5!")
