import pandas as pd
import os

# Dictionary to store rabbit list.
database = {}
# This dictionary contains a name and age as keys and their values are the names of the kitten and ages given by the user. 
# Default age is 'Unknown'

def create_rabbit():
    """
    This function stores a new rabbit's name as both key and value in a dictionary named database if it doesn't exist.
    It also will store the age of the new rabbit as "Unknown".
    If the inputted name already exist in the database, then it will prompt the user to input another name.
    Parameter: None
    Return: Call to function main_menu
    """
    while True: # Function should continuously run once 1 is pressed.
        name = input("Input the new rabbit's name:\n")
        checker = 0 # Used to track if a user given name is in the database
        for rabbit in database:
            if rabbit != name: # Check whether the given name is the same as any of the name in database
                continue
            else:
                checker += 1 # If name is in the databse, increase checker to 1
                break
        if checker > 0:
            print("That name is already in the database.")
        else:
            database.update({name: {'Name': name,'Age':'Unknown','Parent':[],'Kitten':[]}})
            # If a new name is given, update the dictionary with the given name as a value to key 'Name' and 'Unknown' age for the key 'Age'
            return main_menu()
 
def rabbit_age():
    """
    This function updates the 'Age' key in the 'database' dictionary with the user-given value if the rabbit name exists.
    If the name inputted does not exist, it will prompt the user to input another name.
    Parameter: None
    Return: Call to function main_menu
    """
    while True:
        name = input("Input the rabbit's name:\n")
        checker = 0
        for rabbit in database:
            if rabbit == name: # If the rabbit name exists in database then ask for its age
                age = input(f"Input {name}'s age:\n")
                database[rabbit]['Age'] = age # Stores the rabbit's age and replaces 'Unknown'
                break
            else:
                checker += 1 # If name is not in database then increase the count
                continue
        if checker == len(database):
            print("That name is not in the database.")
        else:
            return main_menu()
        
def rabbit_list():
    """
    This function prints the key value pairs of name and age of the rabbits in the database.
    Parameter: None
    Return: None
    """
    for rabbit in database:
        print(rabbit + f" ({database[rabbit]['Age']})")

def parents_kittens():
    """
    This function assign a parent-kitten relationships between the rabbits.
    After taking the names of the parent and kitten pair, it checks the database whether these names exist or not.
    If either of these names does not exist, the function will register the name and update the database with the corresponding relationships.
    If the name exists, it will just update the relationship.
    Parameter: None
    Return: Call to function main_menu
    """    
    parent = input("Input the parent's name:\n")
    kitten = input("Input the kitten's name:\n")

    #The first part of this function deals with checking the inputted parent name and/or updating the relationship with the inputted kitten name
    checker = 0
    for rabbit in database:
        if rabbit != parent:  # This part checks whether any of the rabbit in the database is the parent's
            checker += 1
    if checker == len(database): # If the name is not found in the database, then the name and the relationship is registered as a new key and value.
        database.update({parent : {'Name': parent, 'Age': 'Unknown', 'Parent': [], 'Kitten': [kitten]}})
    else:
        database[parent]['Kitten'] += [kitten] # More kittens are added to the list if the parent is already registered 
        #(considering more than 1 kitten so we store it in a list) 
    database[parent]['Kitten'].sort() # The list of kittens are sorted alphabetically
    
    #The second part of this function deals with checking the inputted kitten name and/or updating the relationship with the inputted parent name
    checker = 0
    for rabbit in database:
        if rabbit != kitten: # This part checks whether any of the rabbit in the database is the kitten's
            checker +=1
    if checker == len(database):# If the name is not found in the database, then the name and the relationship is registered as a new key and value.
        database.update({kitten : {'Name': kitten, 'Age': 'Unknown', 'Parent': [parent], 'Kitten': []}})
    else:
        database[kitten]['Parent'] += [parent] # More kittens are added to the list if the kitten is already registered 
        #(considering 1 kitten can have at most 2 parents so we store it in a list)
    database[kitten]['Parent'].sort() # The list of parents are sorted alphabetically
    return main_menu()

def family_list():
    """
    This function prints the family of a rabbit (parents and kittens) in a alphabetical list.    
    It prompts the user to input a rabbit name until it receives a name that exists in the database.
    Parameter: None
    Return: None
    """
    while True:
        name = input("Input the rabbit's name:\n")
        checker = 0
        for rabbit in database: 
            if rabbit == name: # Checks if the rabbit exist in database
                print(f"Parents of {name}:") 
                if len(database[name]['Parent']) != 0: #If the rabbit have parents registered, it will print the list of parents
                    for parent in database[name]['Parent']:
                        print(parent)
                print(f"Kittens of {name}:")
                if len(database[name]['Kitten']) != 0: #If the rabbit have kittens registered, it will print the list of kittens
                    for kitten in database[name]['Kitten']:
                        print(kitten)
                return main_menu
            else:
                checker += 1
                continue
        if checker == len(database):
            print("That name is not in the database.")

def export_to_excel():
    """
    This function exports the rabbit database to an Excel file.
    It asks the user if they want to name the file or generate it automatically without overwriting existing files.
    """
    if not database:
        print("The database is empty. Nothing to export.")
        return main_menu()
    
    data = []
    for rabbit in database.values():
        data.append({
            'Name': rabbit['Name'],
            'Age': rabbit['Age'],
            'Parents': ', '.join(rabbit['Parent']),
            'Kittens': ', '.join(rabbit['Kitten'])
        })
    
    df = pd.DataFrame(data)

    choice = input("Do you want to input a filename yourself? (yes/no): ").strip().lower()

    if choice == 'yes':
        filename = input("Enter the filename (without extension): ").strip()
        if not filename:
            filename = "rabbit_family"
        filename += ".xlsx"
        
        # Check if file exists already
        counter = 1
        original_filename = filename
        while os.path.exists(filename):
            filename = f"{original_filename[:-5]}_{counter}.xlsx"
            counter += 1

    else:
        # Automatically generate filename
        base_filename = "rabbit_family"
        counter = 1
        filename = f"{base_filename}.xlsx"
        while os.path.exists(filename):
            filename = f"{base_filename}_{counter}.xlsx"
            counter += 1

    df.to_excel(filename, index=False)
    print(f"Database successfully exported to {filename}.")
    return main_menu()

def main_menu():
    """
    This function prints the main menu in which 3 separate functions are called if
    the user enter 0,1,2,3,4 or 5. 
    If user_input is equal to 1 then create_rabbit() is called to register a new rabbit.
    If user_input is equal to 2 then rabbit_age() is called to assign a registered rabbit its age. 
    If user_input is equal to 3 and the database is not empty then rabbit_list() is called to print the registered rabbits' names and ages.
    If the user enters 3 and the database is empty, only "Rabbytes:" is printed.
    If user_input is equal to 4 then parents_kittens() is called to assign or register a parent-kitten relationship to the rabbits.
    If user_input is equal to 5 then family_list() is called to print the families (parents and kittens) of a rabbit.
    If user_input is equal to 6 then export_to_excel() is called to export the family lists to an excel file.
    If the user_input is equal to 0 the program terminates.
    Parameter: None
    Return: None
    """
    while True:
        user_input = input("""==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
6. Export to Excel.
0. Quit.
==================================\n""")
        if user_input == '1':
            create_rabbit()
            continue
        elif user_input == '2':
            rabbit_age()
            continue
        elif user_input == '3':
            print("Rabbytes:")
            if len(database) != 0:
                rabbit_list()
            continue
        elif user_input == '4':
            parents_kittens()
            continue
        elif user_input == '5':
            family_list()
            continue
        elif user_input == '6':
            export_to_excel()
            continue
        elif user_input == '0':
            exit()

main_menu()

