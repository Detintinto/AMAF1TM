import random

# This tuple gets the DNI letter, where the index is the corresponding remainder
DNILetter = ("T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E")

# A dictionary to search for employee data. Each key will be the employee's DNI
EmployeeData = {}

def displayMenuHeader(title, border="*"):
    borderString = "" # Initialize to empty string. Will store the entire menu text.
    for i in range(50):
        borderString += border 
    borderString += "\n" # moves onto the next line of the header
    borderString += border
    
    sizeAdjust = 0
    if len(title) % 2 == 1:
        sizeAdjust = 1
    
    for i in range(24 - int((len(title)+sizeAdjust)/2)):
        borderString += " "
    borderString += title
    for i in range(24 - int((len(title)-sizeAdjust)/2)):
        borderString += " "
  
    borderString += border
    borderString += "\n"
    for i in range(50):
        borderString += border
        
    print(borderString)

def mainMenu(borderStyle):
    exitLoop = False
    while not exitLoop:
        exitLoop = True
        displayMenuHeader("Main Menu", borderStyle)
        print("1.    Employee Management.\n2.    Parts Management.\n3.    Improvements Management.\n4.    Resource Management.\n\nF.    Finish")
        val = input("Please, press an option (1-4, or F): ")
        if val == "1":
            print("You have selected option Employee Management,\n")
        elif val == "2":
            print("You have selected option Parts Management,\n")
        elif val == "3":
            print("You have selected option Improvements Management,\n")
        elif val == "4":
            print("You have selected option Resource Management,\n")
        elif val.lower() == "f":
            print("You have selected to finish from the Main Menu")
        else:
            print("Error: invalid option in the Main Menu,")
            exitLoop = False
    return val.lower()
    
def employeeManagementMenu(borderStyle):
    exitLoop = False
    while not exitLoop:
        exitLoop = True
        displayMenuHeader("Employee Management Menu", borderStyle)
        print("1.    Add Employee.\n2.    Employee List.\n3.    Search Employee by ID.\nB.    Back.\nF.    Finish")
        
        val = input("Please, press an option (1-3, or B, or F): ")
        if val == "1":
            print("You have selected option Add Employee,\n")
        elif val == "2":
            print("You have selected option Employee List,\n")
        elif val == "3":
            print("You have selected option Search Employee by ID,\n")
        elif val.lower() == "b":
            print("Returning to the Main Menu from the Employee Management Menu.\n")
        elif val.lower() == "f":
            print("You have selected to finish from the Employee Management Menu.")
        else:
            print("Error: invalid option in the Employee Management Menu,")
            exitLoop = False
    return val.lower()

def partsManagementMenu(borderStyle):
    exitLoop = False
    while not exitLoop:
        exitLoop = True
        displayMenuHeader("Parts Management Menu", borderStyle)
        print("1.    Add Parts.\n2.    Parts List.\n3.    Search by Parts Group.\nB.    Back.\nF.    Finish")
        
        val = input("Please, press an option (1-3, or B, or F): ")
        if val == "1":
            print("You have selected option Add Parts,\n")
        elif val == "2":
            print("You have selected option Parts List,\n")
        elif val == "3":
            print("You have selected option Search by Parts Group,\n")
        elif val.lower() == "b":
            print("Returning to the Main Menu from the Parts Management Menu.\n")
        elif val.lower() == "f":
            print("You have selected to finish from the Parts Management Menu.")
        else:
            print("Error: invalid option in the Parts Management Menu,")
            exitLoop = False
    return val.lower()

def improvementsManagementMenu(borderStyle):
    exitLoop = False
    while not exitLoop:
        exitLoop = True
        displayMenuHeader("Improvements Management Menu", borderStyle)
        print("1.    Assign Improvement to Development Group.\n2.    Delete Improvement.\nB.    Back\nF.    Finish")
        
        val = input("Please, press an option (1-2, or B, or F): ")
        if val == "1":
            print("You have selected option Assign Improvement to Development Group,\n")
        elif val == "2":
            print("You have selected option Delete Improvement,\n")
        elif val.lower() == "b":
            print("Returning to the Main Menu from the Improvements Management Menu.\n")
        elif val.lower() == "f":
            print("You have selected to finish from the Improvements Management Menu.")
        else:
            print("Error: invalid option in the Improvements Management Menu,")
            exitLoop = False
    return val.lower()
    
def resourceManagementMenu(borderStyle):
    exitLoop = False
    while not exitLoop:
        exitLoop = True
        displayMenuHeader("Resource Management Menu", borderStyle)
        print("1.    Resources Spent.\n2.    Remaining Budget.\nB.    Back.\nF.    Finish")
        
        val = input("Please, press an option (1-2, or B, or F): ")
        if val == "1":
            print("You have selected option Resources Spent,\n")
        elif val == "2":
            print("You have selected option Remaining Budget,\n")
        elif val.lower() == "b":
            print("Returning to the Main Menu from the Resource Management Menu.\n")
        elif val.lower() == "f":
            print("You have selected to finish from the Resource Management Menu.")
        else:
            print("Error: invalid option in the Resource Management Menu,")
            exitLoop = False
    return val.lower()

def addEmployee():
    UserName = ""
    exitLoop = False
    while not exitLoop:
        i = 0 # index for the UserName string, also exit condition! 
        while i == 0:
            UserName = input("Enter your name: ")
            if len(UserName) != 0: # We need to check if it contains at least on letter, "" is not really a name is it?
                i = 1
            else:
                print("This field must include at least one letter.\n")
        UserName = UserName.lower() # This allows us to check just one range, a-z, rather than both A-Z and a-z

        i = 0
        while i < len(UserName):
            if UserName[i] > "0" and UserName[i] < "9": # I will be using this a lot. Check out the ascii table
                i = len(UserName) # Get out of the inner while loop. We avoided more variables ... yay                         
            i+=1 # Note, if the program only finds a-z, then i = UserName.len(), else i = UserName.len()+1
        if i == len(UserName): # Only if UserName contains a-z
            exitLoop = True
            UserName = UserName[0].upper() + UserName[1:]
        else:
            print("This field may only contain letters.\n") 
    exitLoop = False # Don't forget to reset it afterwards, else it won't work a second time!

    UserSurname = ""
    while not exitLoop:
        i = 0
        while i == 0:
            UserSurname = input("Enter your surname: ")
            if len(UserSurname) != 0:
                i = 1
            else:
                print("This field must include at least one letter.\n")
        UserSurname = UserSurname.lower() 

        i = 0 
        while i < len(UserSurname):
            if UserSurname[i] < "a" or UserSurname[i] > "z": 
                i = len(UserSurname) 
            i+=1 
        if i == len(UserSurname): 
            exitLoop = True
            UserSurname = UserSurname[0].upper() + UserSurname[1:]
        else:
            print("This field may only contain letters\n") 
    exitLoop = False 
    
    UserID = ""
    while not exitLoop:
        UserID = input("Enter your ID number: ")
        if UserID.isdigit() and len(UserID) == 8:
            exitLoop = True
        else:
            print("This field may only be an 8 digit number.\n")
    exitLoop = False
    UserID += DNILetter[int(UserID)%23]

    UserAddress = ""
    while not exitLoop:
        UserAddress = input("Enter your address: ")
        if len(UserAddress) >= 3:
            exitLoop = True
        else:
            print("This field must have over 3 characters.\n")
    exitLoop = False
    
    UserPhone = ""
    while not exitLoop:
        UserPhone = input("Enter your phone number: ")
        if UserPhone.isdigit() and len(UserPhone) == 9:
            exitLoop = True
        else:
            print("This field may only be a 9 digit number.\n")
    exitLoop = False

    UserPilot = ""
    while not exitLoop:
        UserPilot = input("Are you a pilot?(y/n): ")
        UserPilot = UserPilot.lower()
        if UserPilot == "y" or UserPilot == "ye" or UserPilot == "yes":
            UserPilot = "Yes"
            exitLoop = True
        elif UserPilot == "n" or UserPilot == "no":
            UserPilot = "No"
            exitLoop = True
        else:
            print("This field may only contain Yes or No.\n")
    exitLoop = False
    
    EmployeeData[UserID] = {"Name":UserName, "Surname":UserSurname, "Address":UserAddress, "Phone":UserPhone, "Pilot":UserPilot} # Store the data

    print("\nEmployee registered:")
    print("Name:   ",     UserName)
    print("Surname:",   UserSurname)
    print("ID:     ",       UserID)
    print("Address:",  UserAddress)
    print("Phone:  ",    UserPhone)
    print("Pilot:  ",    UserPilot) 
    input("Press ENTER to continue.\n")

def employeeList():
    print("Employee list:")
    print("============================")
    for DNI in EmployeeData:
        print(DNI + " " + EmployeeData[DNI]["Name"] + " " + EmployeeData[DNI]["Surname"])
    input("Press ENTER to continue.\n")

def searchEmployee():
    print("Search by employee ID:")
    print("============================")
    UserDNI = input("Enter ID to search: ");
    if UserDNI in EmployeeData:
        print("The employee data with ID " + UserDNI + " are the following:")
        print("Name:    " + EmployeeData[UserDNI]["Name"])
        print("Surname: " + EmployeeData[UserDNI]["Surname"])
        print("Address: " + EmployeeData[UserDNI]["Address"])
        print("Phone:   " + EmployeeData[UserDNI]["Phone"])
        print("Pilot?:  " + EmployeeData[UserDNI]["Pilot"])
    else:
        print("No employee exists with ID " + UserDNI)
    input("Press ENTER to continue.\n") 

def addParts():
    print("Work in progress.\n")

def partsList():
    print("Work in progress.\n")

def searchParts():
    print("Work in progress.\n")

def assignImprovement():
    print("Work in progress.\n")

def deleteImprovement():
    print("Work in progress.\n")

def resourcesSpent():
    print("Work in progress.\n")

def remainingBudget():
    print("Work in progress.\n")

def main():
    
    # Quick and dirty way to add non-uniform probability
    randomBorderBuffer = ("@", "*", "*", "=", "=", "=", "█", "█", "█", "█")
    borderStyle = randomBorderBuffer[random.randint(0, 9)]
    
    exitMain = False
    exitInsideMenu = False
    while not exitMain:
        val = mainMenu(borderStyle)
        if val == "1":
            while not exitInsideMenu:
                val = employeeManagementMenu(borderStyle)
                if val == "1":
                    addEmployee()
                elif val == "2":
                    employeeList()
                elif val == "3":
                    searchEmployee()
                elif val == "b":
                    exitInsideMenu = True
                elif val == "f":
                    exitInsideMenu = True
                    exitMain = True
        elif val == "2":
            while not exitInsideMenu:
                val = partsManagementMenu(borderStyle)
                if val == "1":
                    addParts()
                elif val == "2":
                    partsList()
                elif val == "3":
                    searchParts()
                elif val == "b":
                    exitInsideMenu = True
                elif val == "f":
                    exitInsideMenu = True 
                    exitMain = True
        elif val == "3":
            while not exitInsideMenu:
                val = improvementsManagementMenu(borderStyle)
                if val == "1":
                    assignImprovement()
                elif val == "2":
                    deleteImprovement()
                elif val == "b":
                    exitInsideMenu = True
                elif val == "f":
                    exitInsideMenu = True 
                    exitMain = True
        elif val == "4":
            while not exitInsideMenu:
                val = resourceManagementMenu(borderStyle)
                if val == "1":
                    resourcesSpent()
                elif val == "2":
                    remainingBudget()
                elif val == "b":
                    exitInsideMenu = True
                elif val == "f":
                    exitInsideMenu = True 
                    exitMain = True
        elif val == "f":
            exitMain = True
        exitInsideMenu = False
    
main()
