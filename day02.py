import adventofcode


def run_program(codes, noun = None, verb = None):
    """
    >>> run_program([1, 0, 0, 0, 99])
    [2, 0, 0, 0, 99]
    >>> run_program([2, 3, 0, 3, 99])
    [2, 3, 0, 6, 99]
    >>> run_program([2, 4, 4, 5, 99, 0])
    [2, 4, 4, 5, 99, 9801]
    >>> run_program([1, 1, 1, 4, 99, 5, 6, 0, 99])
    [30, 1, 1, 4, 2, 5, 6, 0, 99]
    """
    ip = 0
    prog = codes.copy()
    prog[1] = noun if noun != None else prog[1]
    prog[2] = verb if verb != None else prog[2]
    while prog[ip] != 99:
        if prog[ip] == 1:
            prog[prog[ip+3]] = prog[prog[ip+1]] + prog[prog[ip+2]]
        elif prog[ip] == 2:
            prog[prog[ip+3]] = prog[prog[ip+1]] * prog[prog[ip+2]]
        ip += 4
    return prog


def brute_force(codes, output):
    for noun in range(100):
        for verb in range(100):
            if run_program(codes, noun, verb)[0] == output:
                return 100 * noun + verb
    return -1


def main():
    puzzle_input = adventofcode.read_input(2)
    codes = [int(code) for code in puzzle_input.split(',')]
    adventofcode.answer(1, 4945026, run_program(codes, 12, 2)[0])
    adventofcode.answer(2, 5296, brute_force(codes, 19690720))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
