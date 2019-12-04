import adventofcode


def is_valid_password_1(password):
    """
    >>> is_valid_password_1("111111")
    True
    >>> is_valid_password_1("223450")
    False
    >>> is_valid_password_1("123789")
    False
    """
    cond1 = False
    cond2 = False
    for c in range(len(password)-1):
        if password[c] == password[c+1]:
            cond1 = True
    if int(password[0]) <= int(password[1]) and int(password[1]) <= int(password[2]) and int(password[2]) <= int(password[3]) and int(password[3]) <= int(password[4]) and int(password[4]) <= int(password[5]):
        cond2 = True
    return cond1 and cond2


def is_valid_password_2(password):
    """
    >>> is_valid_password_2("112233")
    True
    >>> is_valid_password_2("123444")
    False
    >>> is_valid_password_2("111122")
    True
    """
    cond1 = False
    cond2 = False
    if (password[0] == password[1] and password[1] != password[2]) or (password[0] != password[1] and password[1] == password[2] and password[2] != password[3]) or (password[1] != password[2] and password[2] == password[3] and password[3] != password[4]) or (password[2] != password[3] and password[3] == password[4] and password[4] != password[5]) or (password[4] == password[5] and password[3] != password[4]):
        cond1 = True
    if int(password[0]) <= int(password[1]) and int(password[1]) <= int(password[2]) and int(password[2]) <= int(password[3]) and int(password[3]) <= int(password[4]) and int(password[4]) <= int(password[5]):
        cond2 = True
    return cond1 and cond2


def part1(puzzle_input):
    return sum([is_valid_password_1(str(password)) for password in range(int(puzzle_input[0]), int(puzzle_input[1])+1)])


def part2(puzzle_input):
    return sum([is_valid_password_2(str(password)) for password in range(int(puzzle_input[0]), int(puzzle_input[1])+1)])


def main():
    puzzle_input = adventofcode.read_input(4)
    pass_range = puzzle_input.split('-')
    adventofcode.answer(1, 460, part1(pass_range))
    adventofcode.answer(2, 290, part2(pass_range))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
