import json
import time

total_points_reached = 0
total_points_possible = 0


def load_json_from_file(file_name):
    file_name = file_name + ".json" if not file_name.endswith(".json") else file_name
    with open(file_name, "r", encoding="utf-8") as f:
        d = json.load(f)
    print(d)
    print(d.items())
    print("-----")
    print("Completed loading")
    return d


def write_json_to_file(file_name, content):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(content, f, indent="", ensure_ascii=False)


def merge_files(new_file_name):
    file_a = load_json_from_file(input("File 1: "))
    file_b = load_json_from_file(input("File 2: "))
    cards = {"cards": file_a["cards"] + file_b["cards"]}
    write_json_to_file(new_file_name, cards)


def check_answer(c_ans, u_ans):
    correct = 0
    wrong = 0

    for x in c_ans:
        if u_ans.lower().__str__().find(x["answer"].__str__().lower()) < 0:
            wrong += 1
        else:
            correct += 1
            print(x["answer"] + " is correct!")

    global total_points_reached
    total_points_reached += correct
    global total_points_possible
    total_points_possible += len(c_ans)
    print("You got " + correct.__str__()
          + " correct and " + wrong.__str__()
          + " wrong answer(s)"
          )
    print("Possible answer(s): ")
    for a in c_ans:
        print(a["answer"])


def start_questions():
    print("Get ready to answer!")
    file_name = input("Json file name: ")
    cards = load_json_from_file(file_name)
    for x in cards["cards"]:
        print(x["question"])
        check_answer(x["answers"], input("Answer: "))
        time.sleep(1)
    print("You finished all cards!")
    print("Points: " + total_points_reached.__str__()
          + " / "
          + total_points_possible.__str__()
          )


def create_new_card():
    print("Create new card")
    file_name = input("File name: ")
    cards = {"cards": []}
    count = 0
    add_card = True
    while add_card:
        count += 1
        card = {"number": count,
                "question": input("Question: "),
                "answers": []
                }
        add_answer = True
        answers = []
        while add_answer:
            a = {"answer": input("Answer: ")}
            answers.append(a)
            print("Added answer: " + a.__str__())
            if input("Add another answer? (y/n) ") == "n":
                add_answer = False
        card["answers"] = answers
        cards["cards"].append(card)
        print("Added card: " + card.__str__())
        if input("Add another card? (y/n) ") == "n":
            add_card = False
    print("Created " + count.__str__() + " card(s):")
    print(cards)
    write_json_to_file(file_name, cards)


def main_menu():
    print("Welcome to Learning Cards")

    input_acceptable = False
    while not input_acceptable:
        time.sleep(1)
        input_acceptable = True
        print("Menu:")
        print("1 Give me some Questions! \n"
              "2 Create new Cards\n"
              "3 Merge Cards\n"
              "4 end me pls\n"
              )

        match input("Input the number you vibe with:  "):
            case '1':
                # inputAcceptable = True
                print("selected 1")
                start_questions()
                # loadJsonFromFile()
            case '2':
                # inputAcceptable = True
                print("selected 2")
                create_new_card()
            case '3':
                merge_files(input("New file name (.json): "))
            case '4':
                input_acceptable = False
                print("nope")
            case '42':
                input_acceptable = False
                print('YES')
            case _:
                print("That's not an acceptable input! "
                      "Now you have to restart lol")
    main_menu()


if __name__ == '__main__':
    main_menu()