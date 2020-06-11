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
                    fname = input(inputs[inputsIndex])
                    x = fname
                elif(inputsIndex == 1):
                    lname = input(inputs[inputsIndex])
                    x = lname
                elif(inputsIndex == 2):
                    email = input(inputs[inputsIndex])
                    x = email
            else:
                isNum = containsNum(x)
                if(isNum == True):
                    print("\n>>Error: cannot use integers in name field\n")
                    if(inputsIndex == 0):
                        fname = input(inputs[inputsIndex])
                        x = fname
                    elif(inputsIndex == 1):
                        lname = input(inputs[inputsIndex])
                        x = lname
                    elif(inputsIndex == 2):
                        email = input(inputs[inputsIndex])
                        x = email
                else:
                    inputsIndex += 1
                    filePath = open("/users/alex/documents/accts.txt", "a")
                    filePath.write(x + "\n")
                    filePath.close()

                    error = False

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
            print("edit")
        #DELETE
        elif(x == "delete"):
            print("delete")