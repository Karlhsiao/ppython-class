'''

guess num of 1A2B game

by Karl_hsiao

'''

import random

SAMPLE_SPACE = tuple([str(i) for i in range(1, 10)])
DIGIT_LENGTH = 4


def get_user_input(msg):
    input_data = input(msg)
    
    return input_data


def prompt_message(msg):
    print(msg)


def generate_data(sample_space = SAMPLE_SPACE, digit_length = DIGIT_LENGTH):
    data = ""
    indexes = list(range(0, len(sample_space)))
    for i in range(DIGIT_LENGTH):
        sel_idx = random.choice(indexes)
        element = sample_space[sel_idx]
        data += element
        indexes.remove(sel_idx)
    return data


def check_length(input_data, digit_length = DIGIT_LENGTH):
    result = False
    if len(input_data) == digit_length:
        result = True
    return result


def check_unique(input_data, digit_length = DIGIT_LENGTH):
    result = False
    if len(set(input_data)) == digit_length:
        result = True
    return result

def check_validity(input_data, sample_space = SAMPLE_SPACE):
    try:
        float(input_data)
        return True
    except:
        return False

def counts_matches(input_data, true_data, digit_length = DIGIT_LENGTH):
    assert len(input_data) == len(true_data), "The lenght is not correct"
    counts_A = 0
    counts_B = 0
    for t in set(true_data):
        for i in set(input_data):
            if t == i:
                counts_B += 1
    for i in range(digit_length):
        if str(input_data)[i] == str(true_data)[i]:
            counts_A += 1
    counts_B -= counts_A
    return (counts_A, counts_B)


def ask_valid_guess(digit_length = 3):
    while 1:
        msg = "!?"
        input_data = get_user_input("Please input your guess:")

        if check_length(input_data) != True:

            msg = "The guess's length is not correct."

        elif check_validity(input_data) != True:

            msg = "The guess should all be number."

        elif check_unique(input_data) != True:

            msg = f"The {digit_length} number should be unique."

        else:
            break

        prompt_message(msg)

    return input_data

def play_game_human_guess():
    is_match = False
    history = []

    truth = generate_data()

    while 1:
        input_data = ask_valid_guess(DIGIT_LENGTH)
        A, B = counts_matches(input_data, truth)
        history.append((A, B, input_data))
        #print("true anwser:", truth)
        msg = "A:{0} B:{1} guess:{2} #trails:{3}".format(A, B, input_data, len(history))
        prompt_message(msg)
        if A == DIGIT_LENGTH:
            msg = "Correct! #trials:{0}".format(len(history))
            prompt_message(msg)
            break

    return history

if __name__ == "__main__":
    #create a new game
    play_game_human_guess()

    
