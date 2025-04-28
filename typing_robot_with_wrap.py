"""
This program prompt user to input a string for Robbie to type out.
There are 4 configurations of keyboard that Robbie could type on.
For the strings that can be typed out on these configurations, 
this program will pick a suitable keyboard, 
(that is the one with the least actions Robbie need to take)
then plan Robbie's actions. Robbie can also warp around keyboard rows and columns.
For the strings that cannot be typed out, then the program will inform the user.
"""

string_to_type = input("Enter a string to type: ")

# Initializing
config_0 = \
["abcdefghijklm",
 "nopqrstuvwxyz"]

config_1 = \
['789',
 '456',
 '123',
 '0.-']

config_2 = \
["chunk",
 "vibex",
 "gymps",
 "fjord",
 "waltz"] 

config_3 = \
["bemix",
 "vozhd",
 "grypt",
 "clunk",
 "waqfs"]

keyboards = {
    'keyboard0' : config_0,
    'keyboard1' : config_1,
    'keyboard2' : config_2,
    'keyboard3' : config_3
}

Robbie_movements = {
    'up' : 'u',
    'down' : 'd',
    'left' : 'l',
    'right' : 'r',
    'press' : 'p',
    'left warp': 'lw',
    'right warp': 'rw',
    'up warp' : 'uw',
    'down warp' : 'dw'} 
 
Robbie_position = [0,0] # Initial position of Robbie [keyboard,idx]
Robbie_actions = "" 
Robbie_steps = 0
char_index = []
excluded_moves = ['w'] # Since warping are not counted as moves
def pick_config():
    """
    This function checks which configuration of keyboard to use.
    """
    eligible_keyboard = []
    total_moves = []
    real_total_moves = []
    for config_key in keyboards:
        config = keyboards[config_key]
        if all(char in ''.join(config) for char in string_to_type):
            eligible_keyboard.append(config_key)
    total_moves += count_total_moves(eligible_keyboard)
    for moves in total_moves:
        real_total_moves.append([moves[0],remove_warping_moves(moves[1],excluded_moves)]) #exclude warping
    real_total_moves.sort(key= lambda a: len(a[1]))
    for final_moves in total_moves:
        if final_moves[0] == real_total_moves[0][0]:
            picked_moves = final_moves[1]
    picked_config = [real_total_moves[0][0],picked_moves]
    return picked_config

def remove_warping_moves(total_move,excluded_moves):
    """
    This function removes warping actions from Robbie's actions plan.
    """
    for warp_moves in excluded_moves:
        total_move = total_move.replace(warp_moves, "")
    return total_move

def count_total_moves(configs):
    """
    This function count the total moves of each of the eligible keyboard that can type the inputted string.
    """
    char_indexes = []
    counted_moves = []
    Robbie_actions = ''
    Robbie_position = [0,0]
    for config in configs:
        char_indexes.append([config,make_char_index(config)])
    for char_index in char_indexes:
        for [keyboard_lines,idx] in char_index[1]:
            [Robbie_actions_last, Robbie_position_last] = char_vs_Robbie_position(idx,keyboard_lines,Robbie_position,keyboards[char_index[0]][0],keyboards[char_index[0]]) 
            Robbie_position = Robbie_position_last
            Robbie_actions += Robbie_actions_last
        counted_moves.append([char_index[0],Robbie_actions])
    #Restart Robbie_actions and position for the next keyboard configuration
        Robbie_actions = ''
        Robbie_position = [0,0]
    return counted_moves

def make_char_index(config):
    """
    This function make a list of indexes (or coordinates) for the characters from the inputted string
    Each item in the list is another list consisting of two integers.
    The first integer indicates the line in the chosen keyboard where the character is located.
    The second integer indicates the index (the column) in the said line where the character is located.
    """
    char_index = []
    for char in string_to_type:
        for _ in range(len(keyboards[config])):
            if char in keyboards[config][_]:
                char_index.append([_,keyboards[config][_].index(char)]) 
    return char_index

def Robbie_left_right(idx,Robbie_position,keyboard_row):
    """
    This function counts how many left or right actions Robbie need to take.
    The parameters are explained below:
        idx : is the index where the character is positioned on the keyboard line.
        Robbie_position[1] : is the index where Robbie is positioned on the keyboard line.
        keyboard_row : is a row from the keyboard, we just need the length of the row here, 
                        so which row is chosen doesn't matter.
    """
    Robbie_actions = ""
    Robbie_steps = 0
    Robbie_position_now = Robbie_position[1]
    g = (abs(idx - Robbie_position[1]))
    f = int((len(keyboard_row) - 1)/2)
    if (abs(idx - Robbie_position[1])) <= int((len(keyboard_row) - 1)/2):
        if Robbie_position[1] < idx:
            while Robbie_steps < (idx-Robbie_position[1]):
                Robbie_actions += Robbie_movements.get('right')
                Robbie_steps +=1
        elif Robbie_position[1] > idx:
            while Robbie_steps < (Robbie_position[1]-idx):
                Robbie_actions += Robbie_movements.get('left')
                Robbie_steps +=1 
        elif Robbie_position[1] == idx:
            Robbie_actions = ""
    else: 
        if (len(keyboard_row)-1-Robbie_position[1]) < int((len(keyboard_row) - 1)/2):
            while Robbie_position_now < (len(keyboard_row) - 1):
                Robbie_actions += Robbie_movements.get('right')
                Robbie_position_now += 1
            Robbie_actions += Robbie_movements.get('right warp')
            Robbie_position_now = 0 #update Robbie's position into the start of the row    
            while Robbie_position_now < idx:
                Robbie_actions += Robbie_movements.get('right')
                Robbie_position_now += 1
        else:
            while Robbie_position_now > 0 :
                Robbie_actions += Robbie_movements.get('left')
                Robbie_position_now -= 1
            Robbie_actions += Robbie_movements.get('left warp')
            Robbie_position_now = len(keyboard_row) - 1 #update Robbie's position into the end of the row    
            while Robbie_position_now > idx:
                Robbie_actions += Robbie_movements.get('left')
                Robbie_position_now -= 1
    return Robbie_actions

def char_vs_Robbie_position(idx, keyboard_lines, Robbie_position, keyboard_rows, keyboard_column) :
    """
    This function compares Robbie's position and the character index on the selected keyboard configuration,
    then plan what actions should Robbie take to get to each of the character's positions.
    Below is the parameters explained:
        idx : is the index where the character is positioned on the keyboard line.
        keyboard_lines : is the keyboard line where the character is positioned.
        Robbie_position[0] : is the keyboard line where Robbie is positioned.
        keyboard_rows : is a row from the keyboard, we just need the length of the row here, so which row is chosen doesn't matter.
        keyboard_column : is actually the whole configuration of a particular keyboard, we just need the length of the list.
    Below is the output explained:
        Robbie_actions : is the completed plan of action Robbie need to take to type all the inputted string on a particular keyboard.
        Robbie_position : is the last position Robbie's at.
    """
    Robbie_actions = ""
    if Robbie_position[0] == keyboard_lines: # if Robbie already in the right line of keyboard
        Robbie_actions += Robbie_left_right(idx,Robbie_position,keyboard_rows) 
        Robbie_position = [keyboard_lines,idx] # update Robbie's position
    else:
        Robbie_actions += Robbie_left_right(idx,Robbie_position,keyboard_rows)
        Robbie_actions += change_keyboard_lines(Robbie_position[0],keyboard_lines, keyboard_column)[0]
        Robbie_position = [change_keyboard_lines(Robbie_position[0],keyboard_lines, keyboard_column)[1],idx]
    Robbie_actions += Robbie_movements.get('press')
    return Robbie_actions, Robbie_position

def change_keyboard_lines(Robbie_position_now, keyboard_line, keyboard_column):
    """
    This function control Robbie's action if he is not in the right line of the keyboard.
    This function also updates Robbie's position.
    Below is the parameters explained:
        keyboard_line : is the line where the character needed to be type is positioned on the keyboard.
        Robbie_position_now : is the line where Robbie is positioned on the keyboard.
        keyboard_column : is actually the whole configuration of a particular keyboard, we just need the length of the list.
    Below is the output explained.
        Robbie_actions_now : will consists of either up or down moves needed to go to the right line.
        Robbie_pos : is used to update Robbie_position.
    """
    Robbie_actions_now = ''
    f = (abs(keyboard_line - Robbie_position_now))
    g = int((len(keyboard_column) - 1)/2)
    if (abs(keyboard_line - Robbie_position_now)) <= int((len(keyboard_column) - 1)/2):
        if (Robbie_position_now < keyboard_line):
            for _ in range(keyboard_line-Robbie_position_now):
                Robbie_actions_now += Robbie_movements.get('down')
        elif Robbie_position_now > keyboard_line:
            for _ in range(Robbie_position_now-keyboard_line):
                Robbie_actions_now += Robbie_movements.get('up')
    else:
        h =(len(keyboard_column)-1-Robbie_position_now)
        i = int((len(keyboard_column) - 1)/2)
        if (len(keyboard_column)-1-Robbie_position_now) <= int((len(keyboard_column) - 1)/2):
            while Robbie_position_now < (len(keyboard_column) - 1):
                Robbie_actions_now += Robbie_movements.get('down')
                Robbie_position_now += 1
            Robbie_actions_now += Robbie_movements.get('down warp')
            Robbie_position_now = 0 #update Robbie's position into the start of the column    
            while Robbie_position_now < keyboard_line:
                Robbie_actions_now += Robbie_movements.get('down')
                Robbie_position_now += 1
        else:
            while Robbie_position_now > 0 :
                Robbie_actions_now += Robbie_movements.get('up')
                Robbie_position_now -= 1
            Robbie_actions_now += Robbie_movements.get('up warp')
            Robbie_position_now = len(keyboard_column) - 1 #update Robbie's position into the end of the column    
            while Robbie_position_now > keyboard_line:
                Robbie_actions_now += Robbie_movements.get('up')
                Robbie_position_now -= 1
    Robbie_pos = keyboard_line
    return Robbie_actions_now, Robbie_pos

# Check if the inputted string can be typed with any of the keyboard
for config in keyboards:
    eligible = all(char in ''.join(keyboards[config]) for char in string_to_type) 
    if eligible == True:
        break
# If the inputted string can be typed in any of the keyboard, find a suitable keyboard and plan Robbie's actions.    
if  eligible == True:
    picked_config = pick_config()
    print("Configuration used:")
    border = ''
    for _ in range(len(keyboards[picked_config[0]][0]) + 4):
        border += '-'
    print(border,)
    for keyboard_lines in keyboards[picked_config[0]]:
        print("| " + keyboard_lines + " |")
    print(border)
    Robbie_actions = picked_config[1]
    print(f"The robot must perform the following operations:\n{Robbie_actions}")
else:
    print("The string cannot be typed out.")

