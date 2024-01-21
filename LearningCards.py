import json
import time



def startTest(text):
    print(text)

def loadJsonFromFile():
    with open("cards.json", "r") as f:
        d = json.load(f)
    print(d)
    print(d.items())
    print("-----")
    print("Completed loading")
    return d

def testReturn():
    return 'test'

def testPrint():
    print("TestTestTest")

def loadJsonFromString():
    data = json.loads('{"question" : "Test Question Text", "answer" : "Test Answer Text"}')
    print(data[0])

def startQuestions():
    print("Get ready to answer!")
    cards = loadJsonFromFile()
    for x in cards["cards"]:
        print(x["question"])

def createNewCard():
    print("Create new card")

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