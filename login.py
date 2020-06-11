import functions

print("\n")
loop = True
while(loop == True):
    user_request = input("Create, edit, or delete account? - ")
    if user_request in ("create", "edit", "delete"):
        functions.accountAction(user_request) #decides what action user wants ex: (create,add,delete)
    else:
        print("\n>>Error: unknown command '" + user_request + "'\n")
        continue
    loop = False
print("Goodbye!")