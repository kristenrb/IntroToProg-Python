# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Kristen Burke,8/13/2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = ""  # A task entered by user
strPriority = "" # A priority entered by user


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt", "r")
for strData in objFile:
    strTask = strData.split(",")[0].strip()
    strPriority = strData.split(",")[1].strip()
    dicRow = {"Task": strTask, "Priority": strPriority}
    lstTable.append(dicRow)
objFile.close()

# # -- Input/Output -- #
# # Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

#     # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if not lstTable:
            print("To do list is empty! Enjoy your day or add new items.")
            continue  # return to main menu
        else:  # if lstTable has data, do the follow:
            print("Current items on To-Do List:")
            print()
            for dicRow in lstTable:  # loop through lstTable and print row data
                for Task, Priority in dicRow.items():
                    print(Task, " : ", Priority)
        print() # new line for looks
        continue

# Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = str(input("Enter a new task: "))
        strPriority = str(input("Enter a priority level (1 to 5): "))
        print("You entered: " + strTask + " as priority level " + strPriority)
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        continue


# Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strTask = str(input("Which item would you like to remove? (Type BACK to return to menu):  "))
        for row in lstTable:
            if row["Task"] == strTask:
                lstTable.remove(row)
                print("Item deleted")
        if strTask.upper() == "BACK":
            continue
        continue

# Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n")
        objFile.close()
        print("Your data has been saved")
        continue
#
# Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("Goodbye!")
        break  # and Exit the program
