# Strings relating to printing the menu to the user
MainMenuMenu =   '''
****************************************************
*                   Main Menu                      *
****************************************************
1.    Employee Management.
2.    Parts Management.
3.    Improvements Management.
4.    Resource Management.
F.    Finish
'''
EmployeeManagementMenu =   '''
****************************************************
*              Employee Management Menu            *
****************************************************
1.    Add Employee.
2.    Employee List.
3.    Search Employee by ID.
F.    Finish
'''
PartsManagementMenu =   '''
****************************************************
*                Parts Management Menu             *
****************************************************
1.    Add Parts.
2.    Parts List.
3.    Search by Parts Group.
F.    Finish
'''
ImprovementsManagementMenu =   '''
****************************************************
*             Improvements Management Menu         *
****************************************************
1.    Assign Improvement to Development Group.
2.    Delete Improvement.
F.    Finish
'''
ResourceManagementMenu =   '''
****************************************************
*              Resource Management Menu            *
****************************************************
1.    Resources Spent.
2.    Remaining Budget.
F.    Finish
'''


# Strings of menu names and options
MainMenu                = "Main Menu"
EmployeeManagement      = "Employee Management"
PartsManagement         = "Parts Management"
ImprovementsManagement  = "Improvements Management"
ResourceManagement      = "Resource Management"

AddEmployee     = "Add Employee"
EmployeeList    = "Employee List"
SearchEmployee  = "Search Employee by ID"

AddParts    = "Add Parts"
PartsList   = "Parts List"
SearchParts = "Search by Parts Group"

AssignImprovement   = "Assign Improvement to Development Group"
DeleteImprovement   = "Delete Improvement"

ResourcesSpent  = "Resources Spent"
RemainingBudget = "Remaining Budget"


# Strings related to printing the option that was selected
# these can specially be used with the "Strings of menu names and options" defined above to avoid code repetition
InvalidOption   = "Error: invalid option in menu "
MenuFinish      = "You have selected to finish from menu "
OptionSelected  = "You have selected option "


# prints the main menu and get input
print(MainMenuMenu)
val = input("Please, press an option (1-4, or F): ")

# enters the main branch to determine which menu to show
if   val == "1": # EMPLOYEE MANAGEMENT
    print(OptionSelected + EmployeeManagement + ",")
    print(EmployeeManagementMenu)
    val = input("Please, press an option (1-3, or F): ")
    if   val == "1": # ADD EMPLOYEE
        print(OptionSelected + AddEmployee + ",\n")
        UserName    = input("Enter your name: ")
        UserSurname = input("Enter your surname: ")
        UserIDNumber= input("Enter your ID number: ")
        if UserIDNumber.isdigit(): # checking if it is a digit prevents a crash
            UserIDNumber= int(UserIDNumber)
            UserAddress = input("Enter your address: ")
            UserPhone   = input("Enter your phone number: ")
            UserPilot   = input("Are you a pilot?(y/n): ")
            
            UserPilot = UserPilot.lower() # avoids calculating UserPilot.lower() several times
            if   UserPilot == "y" or UserPilot == "ye" or UserPilot == "yes":
                UserPilot = "Yes"
            elif UserPilot == "n" or UserPilot == "no":
                UserPilot = "No"
            else:
                print("\nInvalid answer to pilot ... assume No")
                UserPilot = "No"
            
            rem = UserIDNumber % 23
            if   rem == 0:
                UserIDLetter = "T"
            elif rem == 1:
                UserIDLetter = "R"
            elif rem == 2:
                UserIDLetter = "W"
            elif rem == 3:
                UserIDLetter = "A"
            elif rem == 4:
                UserIDLetter = "G"
            elif rem == 5:
                UserIDLetter = "M"
            elif rem == 6:
                UserIDLetter = "Y"
            elif rem == 7:
                UserIDLetter = "F"
            elif rem == 8:
                UserIDLetter = "P"
            elif rem == 9:
                UserIDLetter = "D"
            elif rem == 10:
                UserIDLetter = "X"
            elif rem == 11:
                UserIDLetter = "B"
            elif rem == 12:
                UserIDLetter = "N"
            elif rem == 13:
                UserIDLetter = "J"
            elif rem == 14:
                UserIDLetter = "Z"
            elif rem == 15:
                UserIDLetter = "S"
            elif rem == 16:
                UserIDLetter = "Q"
            elif rem == 17:
                UserIDLetter = "V"
            elif rem == 18:
                UserIDLetter = "H"
            elif rem == 19:
                UserIDLetter = "L"
            elif rem == 20:
                UserIDLetter = "C"
            elif rem == 21:
                UserIDLetter = "K"
            elif rem == 22:
                UserIDLetter = "E"

            print("\nEmployee registered")
            print("Name: ",     UserName)
            print("Surname:",   UserSurname)
            print("ID: ",       str(UserIDNumber) + UserIDLetter)
            print("Address: ",  UserAddress)
            print("Phone: ",    UserPhone)
            print("Pilot: ",    UserPilot) 
        else: 
            print("Invalid answer to ID number ... exiting")

    elif val == "2": # EMPLOYEE LIST 
        print(OptionSelected + EmployeeList + ",")

    elif val == "3": # SEARCH EMPLOYEE BY ID
        print(OptionSelected + SearchEmployee + ",")

    elif val.lower() == "f":
        print(MenuFinish + EmployeeManagement)

    else: 
        print(InvalidOption + EmployeeManagement)

elif val == "2": # PARTS MANAGEMENT
    print(OptionSelected + PartsManagement + ",") 
    print(PartsManagementMenu)
    val = input("Please, press an option (1-3, or F): ")

    if   val == "1": # ADD PARTS
        print(OptionSelected + AddParts + ",")

    elif val == "2": # PARTS LIST
        print(OptionSelected + PartsList + ",")

    elif val == "3": # SEARCH BY PARTS GROUP
        print(OptionSelected + SearchParts + ",")

    elif val.lower() == "f":
        print(MenuFinish + PartsManagement)

    else: 
        print(InvalidOption + PartsManagement)

elif val == "3": # IMPROVEMENTS MANAGEMENT
    print(OptionSelected + ImprovementsManagement + ",") 
    print(ImprovementsManagementMenu)
    val = input("Please, press an option (1-2, or F): ") 

    if   val == "1": # ASSIGN IMPROVEMENT TO DEVELOPMENT GROUP
        print(OptionSelected + AssignImprovement + ",")

    elif val == "2": # DELETE IMPROVEMENT
        print(OptionSelected + DeleteImprovement + ",")

    elif val.lower() == "f":
        print(MenuFinish + ImprovementsManagement) 

    else: 
        print(InvalidOption + ImprovementsManagement)

elif val == "4": # RESOURCE MANAGEMENT
    print(OptionSelected + ResourceManagement + ",") 
    print(ResourceManagementMenu)
    val = input("Please, press an option (1-2, or F): ")

    if   val == "1": # RESOURCES SPENT
        print(OptionSelected + ResourcesSpent + ",")

    elif val == "2": # REMAINING BUDGET
        print(OptionSelected + RemainingBudget + ",")

    elif val.lower() == "f": 
        print(MenuFinish + ResourceManagement) 

    else: 
        print(InvalidOption + ResourceManagement)

elif val.lower() == "f": # FINISH
    print("You have selected to finish from the Main Menu")

else:
    print("Error: invalid option in the Main Menu") 
