from itertools import permutations
from time import sleep
import threading
import adventofcode


def run_program(codes, prog_input, prog_output = []):
    """
    >>> run_program([3, 0, 4, 0, 99], [1337])
    [1337]
    >>> run_program([3,9,8,9,10,9,4,9,99,-1,8], [8])
    [1]
    >>> run_program([3,9,7,9,10,9,4,9,99,-1,8], [11])
    [0]
    >>> run_program([3,3,1108,-1,8,3,4,3,99], [3])
    [0]
    >>> run_program([3,3,1107,-1,8,3,4,3,99], [-5])
    [1]
    """
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
            while len(prog_input) == 0:
                sleep(0.015)
            prog[prog[ip+1]] = prog_input.pop(0)
            ip += 2
        elif code_and_modes[0] == 4:
            params = get_parameters(1, code_and_modes, prog, ip)
            prog_output.append(params[0])
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
    output = prog_output.copy()
    prog_output.clear()
    return output


def run_program2(codes, prog_input, ip = 0):
    outputs = []
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
            if len(prog_input) == 0:
                return (prog, outputs, ip)
            prog[prog[ip+1]] = prog_input.pop(0)
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
    return (None, outputs, -1)


def get_parameters(num, code_and_modes, prog, ip):
    return [prog[prog[ip+i]] if code_and_modes[i] == 0 else prog[ip+i] for i in range(1, num+1)]


def get_opcode_and_modes(code):
    code_str = str(code).rjust(5, '0')
    return (int(code_str[3:]), int(code_str[2]), int(code_str[1]), int(code_str[0]))


def thruster_signal(codes, sequence):
    a_out = run_program(codes, [sequence[0], 0])[0]
    b_out = run_program(codes, [sequence[1], a_out])[0]
    c_out = run_program(codes, [sequence[2], b_out])[0]
    d_out = run_program(codes, [sequence[3], c_out])[0]
    return run_program(codes, [sequence[4], d_out])[0]


def feedback_mode(codes, sequence):
    """
    >>> feedback_mode([3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5], [9, 8, 7, 6, 5])
    139629729
    """

    a_ip = 0
    b_ip = 0
    c_ip = 0
    d_ip = 0
    e_ip = 0

    a_codes = codes
    b_codes = codes
    c_codes = codes
    d_codes = codes
    e_codes = codes

    a_in = [sequence[0], 0]
    b_in = [sequence[1]]
    c_in = [sequence[2]]
    d_in = [sequence[3]]
    e_in = [sequence[4]]

    e_res = ['dummy']

    while (e_res[0] != None):
        a_res = run_program2(a_codes, a_in, a_ip)
        a_codes = a_res[0]
        a_ip = a_res[2]
        if len(a_res[1]) > 0:
            b_in.append(a_res[1][0])
        b_res = run_program2(b_codes, b_in, b_ip)
        b_codes = b_res[0]
        b_ip = b_res[2]
        if len(b_res[1]) > 0:
            c_in.append(b_res[1][0])
        c_res = run_program2(c_codes, c_in, c_ip)
        c_codes = c_res[0]
        c_ip = c_res[2]
        if len(c_res[1]) > 0:
            d_in.append(c_res[1][0])
        d_res = run_program2(d_codes, d_in, d_ip)
        d_codes = d_res[0]
        d_ip = d_res[2]
        if len(d_res[1]) > 0:
            e_in.append(d_res[1][0])
        e_res = run_program2(e_codes, e_in, e_ip)
        e_codes = e_res[0]
        e_ip = e_res[2]
        if len(e_res[1]) > 0:
            a_in.append(e_res[1][0])
    return e_res[1][0]


def part1(codes):
    max = 0
    sequences = permutations([0, 1, 2, 3, 4])
    for sequence in sequences:
        e_out = thruster_signal(codes, sequence)
        if e_out > max:
            max = e_out
    return max


def part2(codes):
    max = 0
    sequences = permutations([5, 6, 7, 8, 9])
    for sequence in sequences:
        e_out = feedback_mode(codes, sequence)
        if e_out > max:
            max = e_out
    return max


def main():
    puzzle_input = adventofcode.read_input(7)
    codes = [int(code) for code in puzzle_input.split(',')]
    adventofcode.answer(1, 17406, part1(codes))
    adventofcode.answer(2, 1047153, part2(codes))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
