from collections import defaultdict
import adventofcode


def part1(codes):
    prog = defaultdict(int, zip(range(len(codes)), codes))
    output = run_program(prog, [])
    x, y = 0,0
    grid = defaultdict(int)
    for char in output[1]:
        if char == 10:
            y += 1
            x = 0
            continue
        grid[(x,y)] = chr(char)
        x += 1
    params = alignment_parameters(grid)
    total = sum(p[0]*p[1] for p in params)
    return total


def part2(codes):
    # TODO: Calculate programatically
    prog = defaultdict(int, zip(range(len(codes)), codes))
    prog[0] = 2
    inputs = [
        65, 44, 66, 44, 66, 44, 65, 44, 67, 44, 66, 44, 67, 44, 67, 44, 66, 44, 65, 10,
        82, 44, 49, 48, 44, 82, 44, 56, 44, 76, 44, 49, 48, 44, 76, 44, 49, 48, 10,
        82, 44, 56, 44, 76, 44, 54, 44, 76, 44, 54, 10,
        76, 44, 49, 48, 44, 82, 44, 49, 48, 44, 76, 44, 54, 10,
        110, 10
        ]
    output = run_program(prog, inputs)
    return output[1][-1]


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
    puzzle_input = adventofcode.read_input(17)
    codes = [int(code) for code in puzzle_input.split(',')]
    adventofcode.answer(1, 5620, part1(codes))
    adventofcode.answer(1, 768115, part2(codes))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
