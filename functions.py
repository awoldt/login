def createAcct():
    def validateInput(x):
        error = True
        while(error == True):
            if len(x) == 0:
                print("\n>>Error: must enter value\n")
                fname = input("First name: ")
            else:
                error = False

    loop = True
    while(loop == True):
        fname = input("First name: ")
        validateInput(fname)
        lname = input("Last name: ")
        email = input("Email: ")

def accountAction(x):
    global action
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
