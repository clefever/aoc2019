from collections import defaultdict
import adventofcode


def run_program(codes, prog_input):
    """
    >>> run_program([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99], [])
    [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    >>> run_program([1102,34915192,34915192,7,4,7,99,0], [])
    [1219070632396864]
    >>> run_program([104,1125899906842624,99], [])
    [1125899906842624]
    """
    outputs = []
    ip = 0
    relative_base = 0
    prog = defaultdict(int, zip(range(len(codes)), codes))
    while prog[ip] != 99:
        code_and_modes = get_opcode_and_modes(prog[ip])
        if code_and_modes[0] == 1:
            params = get_parameters(2, code_and_modes, prog, ip, relative_base)
            write_loc = get_write_location(3, code_and_modes, prog, ip, relative_base)
            prog[write_loc] = params[0] + params[1]
            ip += 4
        elif code_and_modes[0] == 2:
            params = get_parameters(2, code_and_modes, prog, ip, relative_base)
            write_loc = get_write_location(3, code_and_modes, prog, ip, relative_base)
            prog[write_loc] = params[0] * params[1]
            ip += 4
        elif code_and_modes[0] == 3:
            write_loc = get_write_location(1, code_and_modes, prog, ip, relative_base)
            prog[write_loc] = prog_input.pop(0)
            ip += 2
        elif code_and_modes[0] == 4:
            params = get_parameters(1, code_and_modes, prog, ip, relative_base)
            outputs.append(params[0])
            ip += 2
        elif code_and_modes[0] == 5:
            params = get_parameters(2, code_and_modes, prog, ip, relative_base)
            ip = params[1] if params[0] != 0 else ip + 3
        elif code_and_modes[0] == 6:
            params = get_parameters(2, code_and_modes, prog, ip, relative_base)
            ip = params[1] if params[0] == 0 else ip + 3
        elif code_and_modes[0] == 7:
            params = get_parameters(2, code_and_modes, prog, ip, relative_base)
            write_loc = get_write_location(3, code_and_modes, prog, ip, relative_base)
            prog[write_loc] = 1 if params[0] < params[1] else 0
            ip += 4
        elif code_and_modes[0] == 8:
            params = get_parameters(2, code_and_modes, prog, ip, relative_base)
            write_loc = get_write_location(3, code_and_modes, prog, ip, relative_base)
            prog[write_loc] = 1 if params[0] == params[1] else 0
            ip += 4
        elif code_and_modes[0] == 9:
            params = get_parameters(1, code_and_modes, prog, ip, relative_base)
            relative_base += params[0]
            ip += 2
    return outputs


def get_parameters(num, code_and_modes, prog, ip, relative_base):
    return [prog[prog[ip+i]] if code_and_modes[i] == 0 else prog[ip+i] if code_and_modes[i] == 1 else prog[relative_base+prog[ip+i]] for i in range(1, num+1)]


def get_write_location(write_offset, code_and_modes, prog, ip, relative_base):
    if code_and_modes[write_offset] == 2:
        return relative_base+prog[ip+write_offset]
    else:
        return prog[ip+write_offset]


def get_opcode_and_modes(code):
    code_str = str(code).rjust(5, '0')
    return (int(code_str[3:]), int(code_str[2]), int(code_str[1]), int(code_str[0]))


def main():
    puzzle_input = adventofcode.read_input(9)
    codes = [int(code) for code in puzzle_input.split(',')]
    adventofcode.answer(1, 3013554615, run_program(codes, [1])[0])
    adventofcode.answer(1, 50158, run_program(codes, [2])[0])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
