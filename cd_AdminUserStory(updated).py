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
        addornot = input("Do you want to add a chapter?")
        if addornot == 'no':
            break
        elif addornot == 'yes':
            name = input("the chapters name?")
            chapters[name] = {"definitions": {}, "theorems": {}, "laws": {}, "exercises": {}, "rules": {}}
            print("Now the Chapters are the following")
            for key in chapters:
                print(key)

        else:
            print("please follow the orders")
    return chapters

def addTopics(topics):
    if input("do you want to add something to existing chapters?") == "yes":
        for chapter in topics:
            if input("do you want to modify " + chapter + "?") != "yes":
                continue
            else:
                for category in topics[chapter]:
                    while True:
                        if input("Do you want to add another " + category + "?") != "yes":
                            break
                        else:
                            newTopic = input("what is the name of the " + category + "?")
                            topics[chapter][category][newTopic] = input("write a description for " + newTopic)

    return topics

def changeTopics(topics):
    if input("do you want to change something in existing chapters?") == "yes":
        for chapter in topics:
            if input("do you want to change something in the chapter" + chapter + "?") != "yes":
                continue
            else:
                for category in topics[chapter]:
                    if input("do you want to change a " + category + "?") != "yes":
                        continue
                    else:
                        for definition in topics[chapter][category]:
                            if input("do you want to change definition " + definition + "?") != "yes":
                                continue
                            else:
                                print(definition)
                                print(topics[chapter][category][definition])
                                topics[chapter][category][definition] = input("write new description for" + definition)
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