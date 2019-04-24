import json

def loadCalculusDictionary():
    with open("cd_data.json") as data_file:
        chapters = json.load(data_file)
    return chapters

def chooseTheChapter(chapters):
    print("Here are the chapters")
    for key in chapters:
        print(key)
    chaptersname = input('please enter the name of the chapter that you want')

    chosenchapter = chapters[chaptersname]

    return chosenchapter

def chooseTheCategory(chapter):
    for categories in chapter:
        print(categories)
    categoryname = input('please input whatever you want to access (definition, theorem...)')

    chosencategory = chapter[categoryname]

    return chosencategory

def openTheDescription(category):
    print("here is the information available")
    for description in category:
        print(description)

    descriptionname = input("choose one you want to learn")

    chosendescription = category[descriptionname]

    return chosendescription






def main():
    calculusDictionary = loadCalculusDictionary()
    calculusDictionary = chooseTheChapter(calculusDictionary)
    calculusDictionary = chooseTheCategory(calculusDictionary)
    calculusDictionary = openTheDescription(calculusDictionary)

    print(calculusDictionary)

main()
