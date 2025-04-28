import keyword
import re

# Initialize Python keyword list
kwordlist = keyword.kwlist

# Initialize main menu
menu = """==================================
Enter your choice:
1. Print program.
2. List.
3. Format.
0. Quit.
=================================="""

# Initialize a list to store variable names
program_dict = {'Program': [], 'Var' : [] }
         
def option1():
    """
    This function defines what happens if the user inputs 1 in the main menu.
    It will print the whole program except for the "end" part.
    Parameter: None
    Return: None
    """
    print('Program:')
    print(program_dict['Program'][:-4])
    
def variable_list(new_line: str):
    """
    This function identify and store the variables into a list.
    First it turns the program into a list, then it identify the variable names by:
        1. Keeping the words with underscores in them such as epic_wx or var_x.
        2. Removes special characters such as += = etc and turns them into ''.
        3. Removes python keywords such as for is in etc and turns them into ''
    Lastly it stores the variable names in a dictionary and print each of them.
    Parameter: new_line: str 
    Return: None
    """
    # Initialize a list to store variable names
    variables = new_line.replace('end','') # Exclude the "end" part from the inputted program
    variables = sorted(variables.split()) # Split the string of program by the whitespace so the function can identify each words
    new_variables_copy = variables[:]
    for each_var_index in range(len(new_variables_copy)): # Get rid of the character/word if it is a special character i.e (not new_variables_copy.isalnum()) and not an underscore (not '_' in new_variables_copy)
        if not (new_variables_copy[each_var_index].isalpha()) and (not ('_' in new_variables_copy[each_var_index])): 
            new_variables_copy[each_var_index] = ''

        if new_variables_copy[each_var_index] == '_': # Get rid of unnecessary underscores
            new_variables_copy[each_var_index] = ''

        if (new_variables_copy[each_var_index] in kwordlist): # Get rid of Python keywords
            new_variables_copy[each_var_index] = ''
            
    while '' in new_variables_copy:
        new_variables_copy.remove('') 
    
    for variables in list(dict.fromkeys(new_variables_copy)):
        program_dict['Var'] += [variables] # Removes duplicates and store it in the dictionary 

def option2(): 
    """
    This function prints the list of the variables from the inputted program.
    Parameter: None
    Return: None
    """
    print('Variables:')
    for each_var in program_dict['Var']:
        print(each_var)

def option3():
    """
    This function ask the user to input one of the variables from the list to format it into snake_case format.
    It will prompt the user to input a variable until an existing variable from the list is obtained.
    Parameter: None
    Return: None
    """
    ask_variable_input = input('Pick a variable:\n')

    #condition to check if variable is in list
    while not ask_variable_input in program_dict['Var']:
        print('This is not a variable name.')
        ask_variable_input = input('Pick a variable:\n')
    #stores the index of the variable given by user if in the variables list
    if ask_variable_input in program_dict['Var']:
        store_index = program_dict['Var'].index(ask_variable_input)
    #convert string into list so it is mutable using split

    #convert into snake case
    ask_variable_input_lst_version = list(ask_variable_input)
    for each_letter_index in range(len(ask_variable_input_lst_version)):

        if ask_variable_input_lst_version[each_letter_index].isupper() and each_letter_index == 0:
            ask_variable_input_lst_version[each_letter_index] = ask_variable_input_lst_version[each_letter_index].lower()
    
        elif ask_variable_input_lst_version[each_letter_index].isupper() and each_letter_index > 1:
            ask_variable_input_lst_version[each_letter_index] = '_' + ask_variable_input_lst_version[each_letter_index].lower()

    #convert the list of letters back into a string
    snake_case_word = ''.join(ask_variable_input_lst_version)

    #replace the original variable in variable list
    program_dict['Var'][store_index] = snake_case_word   
    program_dict['Var'] = sorted(program_dict['Var'])

    #replace the original word in the line using Regex
    program_dict['Program'] = re.sub(r'\b' + re.escape(ask_variable_input) + r'\b', snake_case_word, program_dict['Program'])   


def main_menu():
    """
    This function takes the user input in respond to the main menu. It accepts 0,1,2, or 3 as inputs.
    Then it directs each main menu option into its corresponding function.
    Parameter: None
    Return: None
    """
    print(menu)
    user_num_input = input() #accepts 0,1,2, or 3
    while True:
        if user_num_input == '1':
            option1()
            print(menu)
            user_num_input = input() #accepts 0,1,2, or 3
            
        if user_num_input == '2':
            option2()
            print(menu)
            user_num_input = input() #accepts 0,1,2, or 3

        if user_num_input == '3':
            option3()
            print(menu)
            user_num_input = input() #accepts 0,1,2, or 3

        if user_num_input == '0':
            exit()

# Initialize each line of the program
program_lines = ''
# Ask for first line only
first_program_line = input("Enter the Python program to analyze, line by line. Enter {ended} to finish.\n".format(ended="'end'"))
# Separate user input into lines
program_lines += first_program_line 
while True:
    remaining_user_input = input() # Takes rest of input
    program_lines += '\n' + remaining_user_input 
    if 'end' in remaining_user_input:
        break
program_dict['Program'] = program_lines # Store the program lines into the dictionary "program_dict"

# Create the initial variable list and call the main menu.
variable_list(program_lines)
main_menu()
