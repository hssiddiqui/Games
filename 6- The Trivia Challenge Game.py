# This game needs a txt file... Run with Soccertrivia.txt
# To add more questions follow the pattern in the text file otherwise the code will not run properly

def open_file(file_name,mode):
    """Open a file"""
    try:
        the_file = open(file_name,mode)
    except(IOError)as e:
        print("Unable to open file ",file_name,"Ending program.\n",e)
        input("\n\nPress Enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    line= the_file.readline()
    line=line.replace("/","\n")
    return line


def next_block(the_file):
    """Return next line from the trivia file"""
    category = next_line(the_file)
    question = next_line(the_file)

    answers=[]
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    return category,question,answers,correct,explanation


def welcome(title):
    print("Welcome to the Trivia Challenge!\n")
    print("\t\t",title,"\n")


def main():
    trivia_file = open_file("Soccer_trivia.txt","r")
    title=next_line(trivia_file)
    welcome(title)
    score=0

    # Get first block
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t",i+1,") ",answers[i])

        answer= input("What's your answer?: ")

        if answer==correct:
            print("\nRight!")
            score+=1
        else:
            print("\nWrong!")
        print(explanation)
        print("Score: ",score,"\n\n")

        category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()
    print("That was the last question!")
    print("Your final score is: ", score)


main()
input("\n\nPress the enter key to exit.")