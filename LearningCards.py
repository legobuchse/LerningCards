import json
import time


totalPointsReached = 0
totalPointsPossible = 0

def startTest(text):
    print(text)

def loadJsonFromFile(fileName):
    with open(fileName, "r") as f:
        d = json.load(f)
    print(d)
    print(d.items())
    print("-----")
    print("Completed loading")
    return d

def writeJsonToFile(fileName, content):
    with open(fileName, "w") as f:
        json.dump(content, f, indent="", ensure_ascii=False)

def testReturn():
    return 'test'

def testPrint():
    print("TestTestTest")

def loadJsonFromString():
    data = json.loads('{"question" : "Test Question Text", "answer" : "Test Answer Text"}')
    print(data[0])

def checkAnswer(cAns, uAns):

    #answers = uAns.split(uAns, ";", 100)
    correct = 0
    wrong = 0

    for x in cAns:
        if(uAns.__str__().find(x["answer"]) < 0):
            wrong += 1
        else:
            correct += 1
            print(x["answer"] + " is correct!")

    global totalPointsReached
    totalPointsReached += correct
    global totalPointsPossible
    totalPointsPossible += len(cAns)
    print("You got " + correct.__str__() + " correct and " + wrong.__str__() + " wrong answer(s)")
    print("Possible answer(s): ")
    for a in cAns:
        print(a["answer"])

def startQuestions():
    print("Get ready to answer!")
    fileName = input("Json file name: ")
    cards = loadJsonFromFile(fileName)
    for x in cards["cards"]:
        print(x["question"])
        checkAnswer(x["answers"], input("Answer: "))
        time.sleep(1)
    print("You finished all cards!")
    print("Points: " + totalPointsReached.__str__() + " / " + totalPointsPossible.__str__())

def createNewCard():
    print("Create new card")
    fileName = input("File name: ")
    cards = {"cards":[]}
    count = 0
    addCard = True
    while addCard:
        count += 1
        card = {"number":"testNumber","question":"testQuestion","answers":[]}
        card["number"] = count
        card["question"] = input("Question: ")
        addAnswer = True
        answers = []
        #answerObj = {"answer":"testAnswer"}
        while addAnswer:
            a = {"answer":"testAnswer"}
            a["answer"] = input("Answer: ")
            answers.append(a)
            print("Added answer: " + a.__str__())
            if(input("Add another answer? (y/n) ") == "n"):
                addAnswer = False
        card["answers"] = answers
        cards["cards"].append(card)
        print("Added card: " + card.__str__())
        if(input("Add another card? (y/n) ") == "n"):
            addCard = False
    print("Created " + count.__str__() + " card(s):")
    print(cards)
    writeJsonToFile(fileName ,cards)

print("Welcome to Learning Cards")

inputAcceptable = False
while not inputAcceptable:
    time.sleep(1)
    inputAcceptable = True
    print("Menu:")
    print(" 1 Give me some Questions! \n 2 Create new Cards \n 3 end me pls")

    match input("Input the number you vibe with:"):
        case '1':
            # inputAcceptable = True
            print("selected 1")
            startQuestions()
            # loadJsonFromFile()
        case '2':
            # inputAcceptable = True
            print("selected 2")
            createNewCard()
        case '3':
            inputAcceptable = False
            print("nope")
        case '42':
            inputAcceptable = False
            print('YES')
        case other:
            print("Thats not an acceptable Number! Now you have to restart lol")