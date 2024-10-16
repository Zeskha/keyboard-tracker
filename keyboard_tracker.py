from pynput.keyboard import Key, Listener
import json
from threading import Thread, Lock


def main_logic(key, previous_letter, char_list, combination_list):
    actual_letter = key.lower()
    if previous_letter == actual_letter:
        pass
    else:
        if actual_letter:
            char_list.append(actual_letter)
            if previous_letter != "":
                combination_list.append(previous_letter + actual_letter)

            previous_letter = actual_letter

    return char_list, combination_list, previous_letter



def backspace_key_logic(char_list, combination_list, previous_letter):
    if char_list[-1] in [Key.ctrl, Key.ctrl_l, Key.ctrl_r]:
        previous_letter = ""
        return char_list, combination_list, previous_letter
    else:
        if previous_letter:
            char_list.pop(-1)
            try:
                previous_letter = char_list[-1]
            except IndexError:
                previous_letter = ""
            if combination_list:
                combination_list.pop(-1)
            return char_list, combination_list, previous_letter


def save_data(char, comb, lock):
    with lock:
        with open(r"john.json", 'r') as json_input:
            data = json.load(json_input)
            for x in char:
                try:
                    data[x] = int(data[x]) + 1
                except KeyError:
                    pass
            for y in comb:
                try:
                    data[y] = int(data[y]) + 1
                except KeyError:
                    pass

        with open(r"john.json", 'w') as json_output:
            json.dump(data, json_output)


def process_char_list(char_list):
    for i in range(char_list.count(Key.ctrl)):
        char_list.remove(Key.ctrl)
    for i in range(char_list.count(Key.ctrl_r)):
        char_list.remove(Key.ctrl_r)
    for i in range(char_list.count(Key.ctrl_l)):
        char_list.remove(Key.ctrl_l)

    return char_list


def main(key):
    char_list = []
    combination_list = []
    previous_letter = ""
    lock = Lock()

    if key == Key.backspace:
        char_list, combination_list, previous_letter = backspace_key_logic(
                                                        char_list, combination_list, previous_letter)
    elif key in [Key.up, Key.down, Key.right, Key.left, Key.enter, Key.tab]:
        previous_letter = ""

    try:
        char_list, combination_list, previous_letter = main_logic(
            key.char, previous_letter, char_list, combination_list)

    except AttributeError:
        if key in [Key.ctrl, Key.ctrl_l, Key.ctrl_r]:
            char_list.append(key)

    finally:
        if len(char_list) == 50:
            char_list = process_char_list(char_list)
            thread = Thread(target=save_data, args=(char_list, combination_list, lock))
            thread.start()
            char_list = []
            combination_list = []

if __name__ == "__main__":
    with Listener(on_press=main) as listener:
        listener.join()
