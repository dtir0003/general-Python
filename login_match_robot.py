"""
This program prompts user to enter a pair of username and password to login.
Only valid username and password pairs from the predefined list are eligible for login.
If the user fails to provide a correct pair after three attempts, they will
be asked to confirm they are not a robot and given another chance to login.
"""
# Initialize function for user inputs
def user_inputs():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return [username, password]

# Initialize the list of valid usernames and passwords
uname_pw_list = [["Ava", "12345"], ["Leo", "abcde"], ["Raj", "pass1"], ["Zoe", "qwert"], ["Max", "aaaaa"], ["Sam", "zzzzz"], ["Eli", "11111"], ["Mia", "apple"], ["Ian", "hello"], ["Kim", "admin"]]

details = user_inputs()
# Conditioning on whether the user enter the right username and password in the first try,
# iterate the inputted username and password to find a match from the list.  
if details in uname_pw_list:
        print("Login successful. Welcome", details[0],"!")

# If no match found, the program will prompt the user to enter a username and
# password up to two more times, indicating the number of attempts left each time.

else:
    tries = 2
    print("Login incorrect. Tries left:", tries) 
    while tries > 0:
        details = user_inputs()
        if (details in uname_pw_list):
            print("Login successful. Welcome", details[0],"!")
            break 
        else:
            tries -= 1
            print("Login incorrect. Tries left:", tries) 

# When the user exhausts the allowed attempts, they will be asked to confirm they
# are not a robot and will be allowed three more tries.
        if tries == 0:
            robot = ""
            robot_answers = ["Y", ""]
            while True:
                robot = input("Are you a robot (Y/n)? ")
                if robot in robot_answers:
                    break
                elif robot == "n":
                    tries = 3
                    break


