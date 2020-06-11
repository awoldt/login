def createAcct():
    integer = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

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
        error = True
        while(error == True):
            #if user doesn't enter anything
            if len(x) == 0:
                print("\n>>Error: must enter value\n")
                fname = input("First name: ")
                x = fname
            else:
                isNum = containsNum(x)
                if(isNum == True):
                    print("\n>>Error: cannot use integers in name field\n")
                    fname = input("First name: ")
                    x = fname
                else:
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
        else:
            print("\n>>Error: invalid command '" + x + "'\n")
