inputsIndex = 0

def createAcct():
    integer = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    currentInput = "First name: " #default value, user always asked for fname first
    inputs = ("First name: ", "Last name: ", "Email: ")

    #returns true if user input contains integer, false if not 
    def containsNum(x):
        for i in x:
            for y in integer:
                if(i == y):
                    return True
                else:
                    continue
        return False

    #makes sure user input is in correct format
    def validateInput(x):
        global inputsIndex
        error = True
        while(error == True):
            #if user doesn't enter anything
            if len(x) == 0:
                print("\n>>Error: must enter value\n")
                if(inputsIndex == 0):
                    x = input(inputs[inputsIndex])
                elif(inputsIndex == 1):
                    x = input(inputs[inputsIndex])
                elif(inputsIndex == 2):
                    x = input(inputs[inputsIndex])
            else:
                isNum = containsNum(x)
                if(inputsIndex == 2):
                    isNum = False #allows email strings to contain integer 
                #if user fname or lname have a integer in string
                if(isNum == True):
                    print("\n>>Error: cannot use integers in name fields\n")
                    if(inputsIndex == 0):
                        x = input(inputs[inputsIndex])
                    elif(inputsIndex == 1):
                        x = input(inputs[inputsIndex])
                    elif(inputsIndex == 2):
                        x = input(inputs[inputsIndex])   
                #correct input (no errors)
                else:
                    inputsIndex += 1
                    filePath = open("/users/alex/documents/python/login/accts.txt", "a")
                    filePath.write(x + "\n")
                    filePath.close()

                    error = False #ends loop

    loop = True
    while(loop == True):
        fname = input("First name: ")
        validateInput(fname)
        lname = input("Last name: ")
        validateInput(lname)
        email = input("Email: ")
        validateInput(email)
        loop = False
    print("\nAccount created!\n")

def editAccount():
    file = open("/users/alex/documents/python/login/accts.txt", "r")
    text = file.readlines()
    userInputs = tuple(text)
    print(userInputs)
    print(userInputs[0])
    print(userInputs[0][0])
    numOfAccounts = 0

    def compareEmails():
        # finds email data in text file
        letterIndex = 0
        for i in range(len(userInputs)): # i is word ex: "Alex"
            print(i)
            # compare this string to user email input
            if userInputs[i][letterIndex] == "@":
                print("email!")
            
    #counts number of accounts
    for i in range(len(text)):
        string = text[i]
        for y in range(len(string)):
            if string[y] == "@":
                numOfAccounts += 1
    
    print("num of accounts: " + str(numOfAccounts))
    compareEmails()
    file.close()

def accountAction(x):
    actions = ("create", "edit", "delete")
    if len(x) == 0:
        print("\n>>Error: must enter value\n")
    else:
        #CREATE 
        if(x == "create"):
            createAcct()
        #EDIT
        elif(x == "edit"):
            editAccount()
        #DELETE
        elif(x == "delete"):
            print("delete")