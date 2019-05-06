import json

def loadCalculusDictionary():
    with open("cd_data.json") as data_file:
        chapters = json.load(data_file)
    return chapters


def introduction():
    print("Hello dear Admin.\n\nWelcome to Calculus Dictionary. Here you can modify data you have for your application.\n")
    startorclose = input("To start the work type 'go'. To exit type 'close'")
    return startorclose



def addChapters(chapters):
    print("Here are the existing chapters")
    for key in chapters:
        print(key)
    while True:
        addskpiclose = input("To add a chapter insert 'add', to skip type 'skip'")
        if addskpiclose == 'skip':
            break
        elif addskpiclose == 'add':
            name = input("the chapters name?")
            chapters[name] = {"definitions": {}, "theorems": {}, "laws": {}, "exercises": {}, "rules": {}}
            print("Now the Chapters are the following")
            for key in chapters:
                print(key)
        else:
            print("please follow the orders")
    return chapters

def addTopics(topics):
    while True:
        addskipclose = input("To add a topic insert 'add', to skip type 'skip'")
        if addskipclose == 'add':
            for chapter in topics:
                while True:
                    modifyorskip = input("To modify chapter " + chapter + "modify 'modify', to skip type 'skip'")
                    if modifyorskip == 'skip':
                        break
                    elif modifyorskip == 'modify':
                        for category in topics[chapter]:
                            while True:
                                addornot = input("To add another " + category + " type 'add', to skip type 'skip'")
                                if addornot == 'skip':
                                     break
                                elif addornot == 'add':
                                    newTopic = input("what is the name of the " + category + "?")
                                    topics[chapter][category][newTopic] = input("write a description for " + newTopic)
                                else:
                                    print("please follow the orders")
                    else:
                        print("please follow the orders")
        elif addskipclose == 'skip':
            break
        else:
            print("please follow the orders")
    return topics

def changeTopics(topics):
    while True:
        changeornot = input("To change something in existing chapters type 'change', to skip type 'skip'")

        if changeornot == 'skip':
            break
        elif changeornot == 'change':
            for chapter in topics:
                while True:
                    changeorskip = input("To change something in the chapter" + chapter + " type 'change', to skip type 'skip'")
                    if changeorskip == 'skip':
                        break
                    elif changeorskip == 'change':
                        for category in topics[chapter]:
                            while True:
                                changeorcontinue =  input("To change a " + category + " type 'change'")
                                if changeorcontinue == 'skip':
                                    break
                                elif changeorcontinue == 'change':
                                    for definition in topics[chapter][category]:
                                        while True:
                                            yesorno = input("To change definition " + definition + "? (answer 'yes' or 'no'")
                                            if yesorno == "no":
                                                break
                                            elif yesorno == "yes":
                                                print(definition)
                                                print(topics[chapter][category][definition])
                                                topics[chapter][category][definition] = input("write new description for" + definition)
                                            else:
                                                print("please follow the orders")
                                else:
                                    print("please follow the orders")
                    else:
                        print("please follow the orders")
        else:
            print('please follow the orders')
    return topics


def save(data):
    file = open("cd_data.json", "w")
    file.write(json.dumps(data, indent=2))
    file.close()


def main():
    calculusDictionary = loadCalculusDictionary()
    while True:
        startorclose = introduction()
        if startorclose == 'go':
            calculusDictionary = addChapters(calculusDictionary)
            calculusDictionary = addTopics(calculusDictionary)
            calculusDictionary = changeTopics(calculusDictionary)
            save(calculusDictionary)
            break
        elif startorclose == 'close':
            print("The work is finished")
            break
        else:
            print("please follow the orders")

main()
