import json

def loadCalculusDictionary():
    with open("cd_data.json") as data_file:
        chapters = json.load(data_file)
    print("Hello! Welcome to Calculus Dictionarry")
    return chapters

def introduction(chapters):
    while True:
        startorclose = input("\nInsert 'start' to open the chapters, insert 'close' to exit")
        if startorclose == 'start' or startorclose == 'close':
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
        chaptersname = input("\nPlease enter the name of the chapter that you want to examine. To go back type 'back'")
        if chaptersname in chapters[1]:
            chapters = chapters[1][chaptersname]
            break
        elif chaptersname == 'back':
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
        categoryname = input("\nplease input whatever you want to access. If you want to go back to chapters type 'back'")
        if categoryname in chapter[1]:
            chapter = chapter[1][categoryname]
            break
        elif categoryname == 'back':
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
        descriptionname = input("\nType the name of the concept that you want to learn. If you want to go back to categories type 'back'")
        if descriptionname == 'back':
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
        calculusDictionary1 = introduction(initialcalculusDictionary)
        if calculusDictionary1[0] == 'close':
            break
        else:
            while True:
                calculusDictionary2 = chooseTheChapter(calculusDictionary1)
                if calculusDictionary2[0] == 'back':
                    break
                else:
                    while True:
                        calculusDictionary3 = chooseTheCategory(calculusDictionary2)
                        if calculusDictionary3[0] == 'back':
                            break
                        else:
                            while True:
                                calculusDictionary4 = openTheDescription(calculusDictionary3)
                                if calculusDictionary4[0] == 'back':
                                    break
                                else:
                                    print(calculusDictionary4[1])
                                    while True:
                                        if input("\ntype 'back' to go back") == 'back':
                                            break
                                        else:
                                            print("\nPLEASE FOLLOW THE INSTRUCTIONS")

main()
