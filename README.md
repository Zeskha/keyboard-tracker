# Keyboard Tracker
### Description:

The project mainly consists of a relatively simple script that uses the library pyinput for saving all the pressed keys into a JSON file. This counts the times each letter, number, or symbol has been pressed, also storing the combination of pairs of them pressed consecutively. For example, if you pressed the keys "a", "b", and "c"; the values of a, b, and c increase by one, and also will increase by one the combination of "ab" and "cb". The objective for storing these values was for determining the most efficient keyboard distribution, depending on the usage of each letter and counting the combinations for knowing which letter should be next to each other.

The script listens to the keyboard and stores into a list the letter, number, symbols, and ctrl keys pressed. Every time a key is pressed, it will detect which one is pressed. If it is one of the mentioned, it will add it to the pressed_keys list, and if it was a letter written before in the previous_letter variable, a combination of both will be added to the combination_list. Then the key pressed would be stored into the previous_letter variable (this is done for maintaining a constant workflow and avoid possible micro-stress periods when creating all the combination lists at once). The last case doesn't happen if the ctrl key is pressed; in this case, it will only add it to the pressed_keys list. When the maximum characters, in my implementation 50, is reached, it will delete all the ctrls in the pressed_keys list and then start a thread that opens the JSON file, reads data, and sums the times each key is pressed and the combinations for then storing the JSON file. 

It also has logic for backspace, arrows, tab, and enter key pressed. If the backspace is clicked, it will search if ctrl was pressed before; if this is the case, it will just set to "" the variable previous_letter. This is for not adding wrong combinations when deleting high portions of text. If it was no control clicked, it will delete the last combination_list item, set previous_letter to the not erased one, and delete the last item from the char_list. The logic for tab, enter, and arrows is to only set previous_letter to "" for avoiding unreal character combinations when moving through text.

The JSON file contains all characters in ASCII and all the possible combinations between them.

This script is for achieving the best keyboard distribution for a user and the final project for CS50 Introduction to Python course.

