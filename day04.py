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
    has_double = any([password[c] == password[c+1] for c in range(len(password)-1)])
    is_ascending = all([password[c] <= password[c+1] for c in range(len(password)-1)])
    return has_double and is_ascending


def is_valid_password_2(password):
    """
    >>> is_valid_password_2("112233")
    True
    >>> is_valid_password_2("123444")
    False
    >>> is_valid_password_2("111122")
    True
    """
    has_only_double = any(password[c-1] != password[c] and password[c] == password[c+1] and password[c+1] != password[c+2] for c in range(1, len(password)-2)) or (password[0] == password[1] and password[1] != password[2]) or (password[-2] == password[-1] and password[-3] != password[-2])
    is_ascending = all([password[c] <= password[c+1] for c in range(len(password)-1)])
    return has_only_double and is_ascending


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
