toDoList = ["Math Homework", "Cook Dinner", "Fold Laundry"]

def deleteItem(item):
    toDoList.remove(item)
    return toDoList
def addItem(item):
    toDoList.append(item)
    return toDoList

userAns = input("Do you want to add to your list, delete from list, or quit? A/D/Q")
while userAns == "A":
   item = input("What item do you want to add?")
   addItem(item)
   userAns = input("Do you want to add to your list, delete from list, or quit? A/D/Q")
if userAns == "D":
    item = input("Which item would you like to remove?")
    deleteItem(item)
    userAns = input("Do you want to add to your list, delete from list, or quit? A/D/Q")
if userAns == "Q":
    print(toDoList)
    userAns = input("Do you want to add to your list, delete from list, or quit? A/D/Q")
else:
    print(toDoList)
