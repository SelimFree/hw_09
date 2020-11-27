myList = []
try:
    myfile = open("/Users/selim.altayev/Documents/Pecs/El_Programming/Python/hw_09/shopping.txt", "r")
    myList = myfile.read().split("\n")
    myfile.close()
    print("YOUR SHOPPING LIST:")
except FileNotFoundError:
    print("You dont have a list, create a new one")


def printList(myList):
    for item in myList:
        print(item)


def makeList(myList):
    while True:
        choice = input("Wanna add something to the list? (Y/N) ")
        if choice.upper() == "Y":
            newItem = input("Enter the thing you wanna add: ")
            myList.append("- " + newItem)
        elif choice.upper() == "N":
            break
        else: print("INVALID INPUT")


def whatWeBought(myList):
    i = 0
    while i < len(myList):
        weBought = input(f"Have we bought {myList[i]}?  (Y/N)")
        if weBought.upper() == "Y":
            myList[i] = myList[i] + "  ** OK, Purchased"
            i += 1
        elif weBought.upper() == "N":
            i += 1
        else: print("INVALID INPUT")

def writeToFile(myList):
    myfile = open("/Users/selim.altayev/Desktop/shopping.txt", "w")
    myfile.write("\n".join(myList))
    myfile.close()
            

def needToBuy(myList):
    print("Now, we neet to buy:")
    needToBuy = []
    for i in range(len(myList)):
        if "** OK, Purchased" not in myList[i]:
            needToBuy.append(myList[i])
    if len(needToBuy) == 0:
        return 0
    return needToBuy

printList(myList)
makeList(myList)
printList(myList)
whatWeBought(myList)
needToBuy = needToBuy(myList)
if needToBuy != 0: printList(needToBuy)
else: print("We have bought all things")
writeToFile(myList)
