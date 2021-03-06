import json

def loadCalculusDictionary():
    with open("cd_data.json") as data_file:
        chapters = json.load(data_file)
    return chapters

def introduciton(chapters):
    print("Hello dear Admin.\n\nWelcome to Calculus Dictionary. Here you can modify data you have for your application.\n")
    while True:
        startorclose = input("To start working type 'continue', to exit without saving type 'close', to save and close type 'save and close'")
        if (startorclose == 'continue' or startorclose == 'close' or startorclose == 'save and close'):
            decisionandchapters = (startorclose, chapters)
            break
        else:
            print("\nPLEASE FOLLOW THE INSTRUCTIONS!!!")
    return decisionandchapters

def addChapters(chapters):
    print("\nHere are the chapters available\n")
    for key in chapters[1]:
        print("\n", key, "\n")
    while True:
        addChappterOrNot = input("To add a chapter type 'add', to skip this part type 'skip', to close the application without saving type 'close', if you want to save type 'save and close'")
        if (addChappterOrNot == 'close' or addChappterOrNot == 'save and close' or addChappterOrNot == 'skip'):
            break
        elif addChappterOrNot == 'add':
            name = input("the chapters name?")
            chapters[1][name] = {"definitions": {}, "theorems": {}, "laws": {}, "exercises": {}, "rules": {}}
        else:
            print("\nPLEASE FOLLOW THE INSTRUCTIONS!!!")
        print("\nNow the Chapters are the following\n")
        for key in chapters[1]:
            print(key, "\n")
    decisionandchapters = (addChappterOrNot, chapters[1])
    return decisionandchapters

def addTopics(topics):
    while True:
        addTopicorNot = input("\nTo add something in existing chapters type 'add', to skip this part type 'skip', to exit without saving type 'close', to save and exit type 'save and close'")
        if (addTopicorNot == 'close' or addTopicorNot == 'save and close' or addTopicorNot == 'skip'):
            break
        elif addTopicorNot == 'add':
            while True:
                for chapter in topics[1]:
                    print("\n", chapter, "\n")
                chaptername = input("from the following chapters enter the name of a chapter you want to work with, if you are done type 'back")
                if chaptername == 'back':
                    break
                elif chaptername not in topics[1]:
                    print("\nTHERE IS NO SUCH CHAPTER!")
                else:
                    while True:
                        for category in topics[1][chaptername]:
                            print("\n", category, "\n")
                        categoryname = input("now from the following categories write down the name of the one you want to add, if you are done type 'back'")
                        if categoryname == 'back':
                            break
                        elif categoryname not in topics[1][chaptername]:
                            print("\nTHERE IS NO SUCH CATEGORY!")
                        else:
                            while True:
                                for description in topics[1][chaptername][categoryname]:
                                    print("\n", description, "\n")
                                descriptionname = input("enter the name of the new " + categoryname + " if you are done type 'back'")
                                if descriptionname == 'back':
                                    break
                                elif descriptionname in topics[1][chaptername][categoryname]:
                                    print("\n That description already exists")
                                else:
                                    topics[1][chaptername][categoryname][descriptionname] = input("Now dear Admin, please type the description")
        else:
            print("PLEASE FOLLOW THE INSTRUCTIONS!!")
    decisionandchapters = (addTopicorNot, topics[1])
    return decisionandchapters

def changeTopics(topics):
    while True:
        changeorNot = input("To change something in existing chapters type 'change', to skip this part type 'skip', to exit without saving type 'close', to save and exit type 'save and close'")
        if (changeorNot == 'skip' or changeorNot == 'close' or changeorNot == 'save and close'):
            break
        elif changeorNot == 'change':
            while True:
                for chapter in topics[1]:
                    print("\n", chapter, "\n")
                chaptername = input("from the following chapters enter the name of a chapter you want to work with, if you are done type 'back")
                if chaptername == 'back':
                    break
                elif chaptername not in topics[1]:
                    print("\nPLEASE ENTER THE NAME OF A CHAPTER THAT EXISTS")
                else:
                    while True:
                        for category in topics[1][chaptername]:
                            print("\n", category, "\n")
                        categoryname = input("now from the following categories write down the name of the one you want to add, if you are done type 'back'")
                        if categoryname == 'back':
                            break
                        elif categoryname not in topics[1][chaptername]:
                            print("\nTHERE IS NO SUCH CATEGORY!")
                        else:
                            while True:
                                for description in topics[1][chaptername][categoryname]:
                                    print("\n", description, "\n")
                                descriptionname = input("now from the following enter the name of description you want to modify, if you are done type 'back'")
                                if descriptionname == 'back':
                                    break
                                elif descriptionname not in topics[1][chaptername][categoryname]:
                                    print("\n ", descriptionname, " does not exist")
                                else:
                                    print(topics[1][chaptername][categoryname][descriptionname])
                                    topics[1][chaptername][categoryname][descriptionname] = input("enter the new description")
    decisionandchapters = (changeorNot, topics[1])



    return decisionandchapters

def save(data):
    file = open("cd_data.json", "w")
    file.write(json.dumps(data, indent=2))
    file.close()

def main():
    initialcalculusDictionary = loadCalculusDictionary()
    calculusDictionary = introduciton(initialcalculusDictionary)
    while True:
        if calculusDictionary[0] == 'save and close':
            save(calculusDictionary[1])
            break
        elif calculusDictionary[0] == 'close':
            break
        else:
            calculusDictionary = addChapters(calculusDictionary)
            if calculusDictionary[0] == 'save and close':
                save(calculusDictionary[1])
                break
            elif calculusDictionary[0] == 'close':
                break
            else:
                calculusDictionary = addTopics(calculusDictionary)
                if calculusDictionary[0] == 'save and close':
                    save(calculusDictionary[1])
                    break
                elif calculusDictionary[0] == 'close':
                    break
                else:
                    calculusDictionary = changeTopics(calculusDictionary)
                    if calculusDictionary[0] == 'save and close':
                        save(calculusDictionary[1])
                        break
                    elif calculusDictionary[0] == 'close':
                        break
                    else:
                        pass

main()
