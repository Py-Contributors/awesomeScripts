import csv
import random
import platform


def convert_csv_to_dict(file):
    # initialize an empty dict
    question = {}
    # open the csv file
    with open(file, mode="r") as infile:
        # csv.DictReader(f, fieldnames=None, restkey=None,
        # restval=None, dialect='excel',
        # *args, **kwds.)
        reader = csv.reader(infile)
        for row in reader:
            country = row[0]
            capital = row[1]
            question[country] = capital
        return question


def instructions():
    print(
        "\nWelcome To the African Countries Trivia v1.0.0"
        + "\nInstructions:"
        + "\n\tYou have 10 questions to answer "
        + "\n\tAll questions carry equal marks of 5 points each. "
        + "\n\tEnter the answer in the prompt -_ _ _ "
        + "\n\tYou are expected to answer in Title Case "
        + "e.g. 'Washington' but don't worry, any case is accepted"
        + "\n\tOnce you are done,"
        + "you will get a manifest (breakdown) of your result... "
        + "\n\n\tGood luck!"
        + "\n\n Created by Faith Olusegun (a.k.a propenster)"
        + "\n Release Date: June 29th 2020. "
        + "Made with Python "
        + platform.python_version()
        + "\n\n"
    )


def main():
    score = 0
    right = 0
    wrong = 0
    print()
    instructions()
    result = convert_csv_to_dict("african_countries.csv")
    # Convert the keys in the countryDict to a list....
    # country = list(result.keys())
    # #lenghth
    # country_count = int(len(country))
    # #Start the random number generation....
    # country_question = [random.choice(country) for i in range(country_count)]
    # #new question
    # #ensures it's not repeated...
    # question_fresh = [q for q in country if q not in country_question]

    # for i in range(5):
    # 	print(question_fresh)
    for i in range(10):
        chosen = []
        # print a question....from the country dictionary
        question_fresh = list(result.keys())
        r = random.sample(question_fresh, 1)
        if r not in chosen:
            s = ""
            # Convert that list to a string....
            newr = s.join(r)
            # show the user the Question ask for input...
            print("What is the Capital of ", newr)
            answer = str(input("Answer: "))
            if answer.title() in result[newr]:
                print("Correct")
                score += 5
                right += 1
            else:
                print("Incorrect!")
                score = score
                wrong += 1
            chosen.append(r)
        else:
            break
            random.sample(question_fresh, 1)
            i += 1
    # Print User Score Manifest...
    print("\n\n")
    print("Results\n=======")
    print("Right: ", right)
    print("Wrong: ", wrong)
    print("Your Total Score is ", score, " point(s)")
    print("\nThank you for playing the African Countries Trivia Game")


if __name__ == "__main__":
    main()
