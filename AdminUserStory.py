import json

with open("data.json") as data_file:
    data = json.load(data_file)

print("Here are the chapters available")

for key in data:
    print(key)

#adding a chapter
while True:
    answer = input("insert 1 to add a chapter. insert 2 to continue without adding")
    if answer != "1":
        break
    else:
        name = input("the chapters name?")
        data[name] = {"definitions":{}, "theorems":{}, "laws":{},"exercises":{},"rules": {}}
        file = open("data.json", "w")
        file.write(json.dumps(data, indent=2))
        file.close()
        print("now you have the following chapters")
        for key in data:
            print(key)

#choosing a chapter

for i in data:
    print("chapter", i)
    a = input("do you want to modify?")
    if a == "1":
        for j in data[i]:
            print(j)
            a = input("1 to add, 2 too modify, 3 continue")
            if a == "1":
                defname = input("name of definition")
                data[i][j][defname] = input("write the content")
                file = open("data.json", "w")
                file.write(json.dumps(data, indent=2))
                file.close()
            #elif a == 2:
            #elif a == 3:
            #these are questions I want to ask
            else:
                break
    else:
        break

# also I could not make this with functions because some errors came out idk...
# I did not handle to make the whole story I have a lot of questions about it.














