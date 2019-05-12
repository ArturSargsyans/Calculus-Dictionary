import json

def loadCalculusDictionary():
    with open("cd_data.json") as data_file:
        chapters = json.load(data_file)
    print("Hello! Welcome to Calculus Dictionarry")
    return chapters

def introduction(chapters):
    while True:
        startorclose = input("\nInsert 'start' to open the chapters")
        if startorclose == 'start':
            decisionandchapters = (startorclose, chapters)
            break
        else:
            print("PLEASE FOLLOW THE INSTRUCTIONS")
    return decisionandchapters


def chooseTheChapter(chapters):
    print("Here are the chapters available")
    for key in chapters[1]:
        print("\n", key, "\n")
    while True:
        chaptersname = input("\nPlease enter the name of the chapter that you want to examine. To exit type 'close'")
        if chaptersname in chapters[1]:
            chapters = chapters[1][chaptersname]
            break
        elif chaptersname == 'close':
            break
        else:
            print("\nTHAT CHAPTER DOES NOT EXIST!, please try again")
    decisionandchapter = (chaptersname, chapters)
    return decisionandchapter

def chooseTheCategory(chapter):
    while True:
        print("Here are the categories")
        for categories in chapter[1]:
            print("\n", categories, "\n")
        categoryname = input("\nplease input whatever you want to access. if you want to exit type 'close'")
        if categoryname in chapter[1]:
            chapter = chapter[1][categoryname]
            break
        elif categoryname == 'close':
            break
        else:
            print("\nThere is no such category. Please try again")
    decisionandcategory = (categoryname, chapter)
    return decisionandcategory

def openTheDescription(category):
    print("Here is the information available")
    while True:
        for description in category[1]:
            print("\n", description, "\n")
        descriptionname = input("\nType the name of the concept that you want to learn. If you want to exit type 'close'")
        if descriptionname == 'close':
            break
        elif descriptionname in category[1]:
            category = category[1][descriptionname]
            break
        else:
            print("\nTHERE IS NO SUCH THING IN THE LIST. PLEASE TRY AGAIN")
    decisionanddescription = (descriptionname, category)
    return decisionanddescription






def main():
    initialcalculusDictionary = loadCalculusDictionary()
    while True:
        calculusDictionary = introduction(initialcalculusDictionary)
        calculusDictionary = chooseTheChapter(calculusDictionary)
        if calculusDictionary[0] == 'close':
            break
        else:
            calculusDictionary = chooseTheCategory(calculusDictionary)
            if calculusDictionary[0] == 'close':
                break
            else:
                calculusDictionary = openTheDescription(calculusDictionary)
                if calculusDictionary[0] == 'close':
                    break
                else:
                    print(calculusDictionary[1])


main()
