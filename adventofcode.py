# Author: Keith Wissing
from termcolor import colored


def read_input(day):
    puzzle_input = [line.rstrip('\n') for line in open("day%02d_input.txt" % day)]
    if len(puzzle_input) == 1:
        puzzle_input = puzzle_input[0]
    return puzzle_input


def answer(part, correct, calculated):
    if correct == 0:
        color = 'yellow'
    elif calculated == correct:
        color = 'green'
    else:
        color = 'red'
    message = "Part %d Answer %s" % (part, calculated)
    print(colored(message, color))
