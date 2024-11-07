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
B.    Back.
F.    Finish
'''
PartsManagementMenu =   '''
****************************************************
*                Parts Management Menu             *
****************************************************
1.    Add Parts.
2.    Parts List.
3.    Search by Parts Group.
B.    Back.
F.    Finish
'''
ImprovementsManagementMenu =   '''
****************************************************
*             Improvements Management Menu         *
****************************************************
1.    Assign Improvement to Development Group.
2.    Delete Improvement.
B.    Back
F.    Finish
'''
ResourceManagementMenu =   '''
****************************************************
*              Resource Management Menu            *
****************************************************
1.    Resources Spent.
2.    Remaining Budget.
B.    Back.
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

# This tuple gets the DNI letter, where the index is the corresponding remainder
DNILetter = ("T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E")

# A dictionary to search for employee data. Each key will be the employee's DNI
EmployeeData = {}

# Exit condition for all loop. Why can't we use break again? :(
MainMenuExit = False
EmployeeManagementExit = False
PartsManagementExit = False
ImprovementsManagementExit = False
ResourceManagementExit = False

InputPromptExit = False # This one is used when gathering input in add employee

while not MainMenuExit:

    print(MainMenuMenu)
    val = input("Please, press an option (1-4, or F): ")

    # enters the main branch to determine which menu to show vvvvv

    if val == "1": # EMPLOYEE MANAGEMENT
        print(OptionSelected + EmployeeManagement + ",") # It should only be printed once, so I'll put it here

        while not EmployeeManagementExit:

            print(EmployeeManagementMenu)
            val = input("Please, press an option (1-3, or B or F): ")

            if   val == "1": # ADD EMPLOYEE
                print(OptionSelected + AddEmployee + ",\n")

                UserName = ""
                while not InputPromptExit:
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
                        if UserName[i] < "a" or UserName[i] > "z": # I will be using this a lot. Check out the ascii table
                            i = len(UserName) # Get out of the inner while loop. We avoided more variables ... yay                         
                        i+=1 # Note, if the program only finds a-z, then i = UserName.len(), else i = UserName.len()+1
                    if i == len(UserName): # Only if UserName contains a-z
                        InputPromptExit = True
                        UserName = UserName[0].upper() + UserName[1:]
                    else:
                        print("This field may only contain letters.\n") 
                InputPromptExit = False # Don't forget to reset it afterwards, else it won't work a second time!
            
                UserSurname = ""
                while not InputPromptExit:
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
                        InputPromptExit = True
                        UserSurname = UserSurname[0].upper() + UserSurname[1:]
                    else:
                        print("This field may only contain letters\n") 
                InputPromptExit = False 
                
                UserID = ""
                while not InputPromptExit:
                    UserID = input("Enter your ID number: ")
                    if UserID.isdigit() and len(UserID) == 8:
                        InputPromptExit = True
                    else:
                        print("This field may only be an 8 digit number.\n")
                InputPromptExit = False
                UserID += DNILetter[int(UserID)%23]

                UserAddress = ""
                while not InputPromptExit:
                    UserAddress = input("Enter your address: ")
                    if len(UserAddress) >= 3:
                        InputPromptExit = True
                    else:
                        print("This field must have over 3 characters.\n")
                InputPromptExit = False
                
                UserPhone = ""
                while not InputPromptExit:
                    UserPhone = input("Enter your phone number: ")
                    if UserPhone.isdigit() and len(UserPhone) == 9:
                        InputPromptExit = True
                    else:
                        print("This field may only be a 9 digit number.\n")
                InputPromptExit = False

                UserPilot = ""
                while not InputPromptExit:
                    UserPilot = input("Are you a pilot?(y/n): ")
                    UserPilot = UserPilot.lower()
                    if UserPilot == "y" or UserPilot == "ye" or UserPilot == "yes":
                        UserPilot = "Yes"
                        InputPromptExit = True
                    elif UserPilot == "n" or UserPilot == "no":
                        UserPilot = "No"
                        InputPromptExit = True
                    else:
                        print("This field may only contain Yes or No.\n")
                InputPromptExit = False
                
                EmployeeData[UserID] = {"Name":UserName, "Surname":UserSurname, "Address":UserAddress, "Phone":UserPhone, "Pilot":UserPilot} # Store the data

                print("\nEmployee registered")
                print("Name:   ",     UserName)
                print("Surname:",   UserSurname)
                print("ID:     ",       UserID)
                print("Address:",  UserAddress)
                print("Phone:  ",    UserPhone)
                print("Pilot:  ",    UserPilot) 
                input("Press ENTER to continue.")

            elif val == "2": # EMPLOYEE LIST 
                print("Employee list:")
                print("============================")
                for DNI in EmployeeData:
                    print(DNI + " " + EmployeeData[DNI]["Name"] + " " + EmployeeData[DNI]["Surname"])
                input("Press ENTER to continue.")


            elif val == "3": # SEARCH EMPLOYEE BY ID
                print("Search by employee ID:")
                print("============================")
                UserDNI = input("Enter ID to search: ");
                if UserDNI in EmployeeData:
                    print("The employee data with ID " + UserDNI + " are the following:")
                    print("Name:    " + EmployeeData[DNI]["Name"])
                    print("Surname: " + EmployeeData[DNI]["Surname"])
                    print("Address: " + EmployeeData[DNI]["Address"])
                    print("Phone:   " + EmployeeData[DNI]["Phone"])
                    print("Pilot?:  " + EmployeeData[DNI]["Pilot"])
                else:
                    print("No employee exists with ID " + UserDNI)
                input("Press ENTER to continue.")

            elif val.lower() == "b":
                print("Returning to the " + MainMenu + " from the " + EmployeeManagement + " Menu.")
                EmployeeManagementExit = True

            elif val.lower() == "f":
                print(MenuFinish + EmployeeManagement)
                print("End")
                EmployeeManagementExit = True
                MainMenuExit = True

            else: 
                print(InvalidOption + EmployeeManagement)

    elif val == "2": # PARTS MANAGEMENT
        print(OptionSelected + PartsManagement + ",") 
        print(PartsManagementMenu)
        while not PartsManagementExit:
            val = input("Please, press an option (1-3, or B or F): ")

            if   val == "1": # ADD PARTS
                print(OptionSelected + AddParts + ",")

            elif val == "2": # PARTS LIST
                print(OptionSelected + PartsList + ",")

            elif val == "3": # SEARCH BY PARTS GROUP
                print(OptionSelected + SearchParts + ",")

            elif val.lower() == "b":
                print("Returning to the " + MainMenu + " from the " + PartsManagement + " Menu.")
                PartsManagementExit = True

            elif val.lower() == "f":
                print(MenuFinish + PartsManagement)
                print("End")
                PartsManagementExit = True
                MainMenuExit = True

            else: 
                print(InvalidOption + PartsManagement)

    elif val == "3": # IMPROVEMENTS MANAGEMENT
        print(OptionSelected + ImprovementsManagement + ",") 
        print(ImprovementsManagementMenu)
        while not ImprovementsManagementExit:
            val = input("Please, press an option (1-2, or B or F): ") 

            if   val == "1": # ASSIGN IMPROVEMENT TO DEVELOPMENT GROUP
                print(OptionSelected + AssignImprovement + ",")

            elif val == "2": # DELETE IMPROVEMENT
                print(OptionSelected + DeleteImprovement + ",")

            elif val.lower() == "b":
                print("Returning to the " + MainMenu + " from the " + ImprovementsManagement + " Menu.")
                ImprovementsManagementExit = True  

            elif val.lower() == "f":
                print(MenuFinish + ImprovementsManagement) 
                print("End") 
                ImprovementsManagementExit = True
                MainMenuExit = True

            else: 
                print(InvalidOption + ImprovementsManagement)

    elif val == "4": # RESOURCE MANAGEMENT
        print(OptionSelected + ResourceManagement + ",") 
        print(ResourceManagementMenu)
        while not ResourceManagementExit:
            val = input("Please, press an option (1-2, or B or F): ")

            if   val == "1": # RESOURCES SPENT
                print(OptionSelected + ResourcesSpent + ",")

            elif val == "2": # REMAINING BUDGET
                print(OptionSelected + RemainingBudget + ",")

            elif val.lower() == "b":
                print("Returning to the " + MainMenu + " from the " + ResourceManagement + " Menu.")
                ResourceManagementExit = True 

            elif val.lower() == "f": 
                print(MenuFinish + ResourceManagement) 
                print("End")
                ResourceManagementExit = True
                MainMenuExit = True

            else: 
                print(InvalidOption + ResourceManagement)

    elif val.lower() == "f": # FINISH
        print("You have selected to finish from the Main Menu\nEnd")
        MainMenuExit = True
    else:
        print("Error: invalid option in the Main Menu") 

    # The only way to exit the loops are for these conditions to be True
    # We must reset them afterwards
    EmployeeManagementExit = False
    PartsManagementExit = False
    ImprovementsManagementExit = False
    ResourceManagementExit = False
