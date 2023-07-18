from mlconjug3 import Conjugator

# initialize the conjugator
language = input("select language (pt fr es it pt ro): ")
print("\n")
conjugator = Conjugator(language=language)

while True:
    print("Note: write 'exit' to exit.")
    inputted = input("Select verb to conjugate: ")

    if inputted == "exit":
        break

    verb = conjugator.conjugate(inputted)
    # print(verb.iterate())  # prints the whole thing

    # if language == "ro":
    #     print("\n")
    #     print(inputted, "\n")
    #     for mood in verb.iterate():
    #         if 'Mai' in mood[0]:
    #             print(mood[0], mood[1], "Mai mult ca perfect", mood[3])



    print("List of all tenses: \n")
    verb_list = verb.iterate()
    for item in verb_list:
        print(item)
