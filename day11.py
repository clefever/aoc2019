from collections import defaultdict
import adventofcode


def part1(codes):
    curr_pos = (0, 0)
    curr_direction = 0 # Up = 0, Right = 1, Down = 2, Left = 3
    grid = defaultdict(int)
    painted = set()
    prog = defaultdict(int, zip(range(len(codes)), codes))
    prog_output = (prog, [], 0, 0)
    while True:
        prog_output = run_program(prog_output[0], [grid[curr_pos]], prog_output[2], prog_output[3])
        if prog_output[0] != None:
            grid[curr_pos] = prog_output[1][0]
            painted.add(curr_pos)
            direction_change = -1 if prog_output[1][1] == 0 else 1
            curr_direction = (curr_direction + direction_change) % 4
            change = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}[curr_direction]
            curr_pos = (curr_pos[0] + change[0], curr_pos[1] + change[1])
        else:
            break
    return len(painted)


def part2(codes):
    curr_pos = (0, 0)
    curr_direction = 0 # Up = 0, Right = 1, Down = 2, Left = 3
    grid = defaultdict(int)
    grid[curr_pos] = 1
    prog = defaultdict(int, zip(range(len(codes)), codes))
    prog_output = (prog, [], 0, 0)
    while True:
        prog_output = run_program(prog_output[0], [grid[curr_pos]], prog_output[2], prog_output[3])
        if prog_output[0] != None:
            grid[curr_pos] = prog_output[1][0]
            direction_change = -1 if prog_output[1][1] == 0 else 1
            curr_direction = (curr_direction + direction_change) % 4
            change = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}[curr_direction]
            curr_pos = (curr_pos[0] + change[0], curr_pos[1] + change[1])
        else:
            break

    left = min([key[0] for key in grid.keys()])
    right = max([key[0] for key in grid.keys()])
    bottom = max([key[1] for key in grid.keys()])
    top = min([key[1] for key in grid.keys()])

    for y in range(top, bottom+1):
        for x in range(left, right+1):
            if grid[(x,y)] == 1:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()


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
    puzzle_input = adventofcode.read_input(11)
    codes = [int(code) for code in puzzle_input.split(',')]
    adventofcode.answer(1, 2016, part1(codes))
    adventofcode.answer(1, "RAPRCBPH", part2(codes))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
