import adventofcode


def run_program(codes, prog_input):
    """
    >>> run_program([3, 0, 4, 0, 99], 1337)
    [1337]
    >>> run_program([3,9,8,9,10,9,4,9,99,-1,8], 8)
    [1]
    >>> run_program([3,9,7,9,10,9,4,9,99,-1,8], 11)
    [0]
    >>> run_program([3,3,1108,-1,8,3,4,3,99], 3)
    [0]
    >>> run_program([3,3,1107,-1,8,3,4,3,99], -5)
    [1]
    """
    outputs = []
    ip = 0
    prog = codes.copy()
    while prog[ip] != 99:
        code_and_modes = get_opcode_and_modes(prog[ip])
        if code_and_modes[0] == 1:
            params = get_parameters(2, code_and_modes, prog, ip)
            prog[prog[ip+3]] = params[0] + params[1]
            ip += 4
        elif code_and_modes[0] == 2:
            params = get_parameters(2, code_and_modes, prog, ip)
            prog[prog[ip+3]] = params[0] * params[1]
            ip += 4
        elif code_and_modes[0] == 3:
            prog[prog[ip+1]] = prog_input
            ip += 2
        elif code_and_modes[0] == 4:
            params = get_parameters(1, code_and_modes, prog, ip)
            outputs.append(params[0])
            ip += 2
        elif code_and_modes[0] == 5:
            params = get_parameters(2, code_and_modes, prog, ip)
            ip = params[1] if params[0] != 0 else ip + 3
        elif code_and_modes[0] == 6:
            params = get_parameters(2, code_and_modes, prog, ip)
            ip = params[1] if params[0] == 0 else ip + 3
        elif code_and_modes[0] == 7:
            params = get_parameters(2, code_and_modes, prog, ip)
            prog[prog[ip+3]] = 1 if params[0] < params[1] else 0
            ip += 4
        elif code_and_modes[0] == 8:
            params = get_parameters(2, code_and_modes, prog, ip)
            prog[prog[ip+3]] = 1 if params[0] == params[1] else 0
            ip += 4
    return outputs


def get_parameters(num, code_and_modes, prog, ip):
    return [prog[prog[ip+i]] if code_and_modes[i] == 0 else prog[ip+i] for i in range(1, num+1)]


def get_opcode_and_modes(code):
    code_str = str(code).rjust(5, '0')
    return (int(code_str[3:]), int(code_str[2]), int(code_str[1]), int(code_str[0]))


def main():
    puzzle_input = adventofcode.read_input(5)
    codes = [int(code) for code in puzzle_input.split(',')]
    adventofcode.answer(1, 6731945, run_program(codes, 1)[-1])
    adventofcode.answer(2, 9571668, run_program(codes, 5)[0])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
