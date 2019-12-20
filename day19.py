from collections import defaultdict
import adventofcode


def part1(codes):
    prog = defaultdict(int, zip(range(len(codes)), codes))
    total_pulled = 0
    for y in range(50):
        for x in range(50):
            output = run_program(prog, [x, y])
            total_pulled += output[1][0]
    return total_pulled


def part2(codes):
    # TODO: Calculate programatically
    prog = defaultdict(int, zip(range(len(codes)), codes))
    grid = defaultdict(int)
    x_pos, y_pos = 918, 1022
    for y in range(y_pos, y_pos+100):
        for x in range(x_pos, x_pos+100):
            output = run_program(prog, [x, y])
            grid[(x,y)] = output[1][0]
    #print_grid(grid)
    return x_pos * 10000 + y_pos


def print_grid(grid):
    left = min([key[0] for key in grid.keys()])
    right = max([key[0] for key in grid.keys()])
    bottom = max([key[1] for key in grid.keys()])
    top = min([key[1] for key in grid.keys()])

    for y in range(top, bottom+1):
        for x in range(left, right+1):
            print(grid[(x,y)], end=" ")
        print()


def alignment_parameters(grid):
    left = min([key[0] for key in grid.keys()])
    right = max([key[0] for key in grid.keys()])
    bottom = max([key[1] for key in grid.keys()])
    top = min([key[1] for key in grid.keys()])

    param_list = []

    for y in range(top+1, bottom):
        for x in range(left+1, right):
            if grid[(x,y)] == '#' and grid[(x-1,y)] == '#' and grid[(x+1,y)] == '#' and grid[(x,y-1)] == '#' and grid[(x,y+1)] == '#':
                param_list.append((x,y))

    return param_list


def run_program(codes, prog_input, ip = 0, relative_base = 0):
    outputs = []
    prog = codes.copy()
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
            if len(prog_input) == 0:
                return (prog, outputs, ip, relative_base)
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
    return (None, outputs, -1, -1)


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
    puzzle_input = adventofcode.read_input(19)
    codes = [int(code) for code in puzzle_input.split(',')]
    adventofcode.answer(1, 197, part1(codes))
    adventofcode.answer(1, 9181022, part2(codes))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
