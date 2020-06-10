import functions

print("\n")
loop = True
while(loop == True):
    user_request = input("Create, edit, or delete account? - ")
    functions.accountAction(user_request) #decides what action user wants ex: (create,add,delete)