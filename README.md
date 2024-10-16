Phase: 1

Functional Description: Displays a simpe menu asking for input in the form of an option to select. This then takes you to different menus, such as the Parts Management Menu. Specifically in the Employee Management Menu, you can select the option to add a new employee, and get prompted with several pieces of information for this new employee.

Code Decription: The strings that will be repeated or and very big are first stored in variables near the top. This allows for reusabiliy and readability. 
The main menu is printed and then input is prompted. With an if - elif - else structure, the program determines if the input is a valid number , F, or nonsense.Inside each valid number, it prints the corresponding menu screen, and splits the value of a new input prompt in the corresponding possible options. Specifically, in the Employee Management menu, the "Add employee" option is somewhat functional in this phase. It gathers input in variables and then prints them out. As for the letter after the ID number, that is calculated by maching the remainder mod 23 with the corresponding number.
