import adventofcode


class Coordinate:
    def __init__(self, x, y, wire_num, steps):
        self.x = x
        self.y = y
        self.wire_flags = 1 << (wire_num - 1)
        self.steps = {wire_num: steps}


def intersect_distance(wire1, wire2):
    """
    >>> intersect_distance(['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4'])
    6
    >>> intersect_distance(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'], ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'])
    159
    >>> intersect_distance(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'], ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'])
    135
    """
    coords = intersections(wire1, wire2)
    min_coord = min(coords, key=lambda coord: abs(coord.x) + abs(coord.y))
    return abs(min_coord.x) + abs(min_coord.y)


def intersect_min_steps(wire1, wire2):
    """
    >>> intersect_min_steps(['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4'])
    30
    >>> intersect_min_steps(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'], ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'])
    610
    >>> intersect_min_steps(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'], ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'])
    410
    """
    coords = intersections(wire1, wire2)
    min_coord = min(coords, key=lambda coord: coord.steps[1] + coord.steps[2])
    return min_coord.steps[1] + min_coord.steps[2]


def intersections(wire1, wire2):
    coord_dict = {}
    wire_num = 0
    for wire in [wire1, wire2]:
        curr_coord = Coordinate(0, 0, 1, 0)
        wire_num += 1
        step = 0
        for seg in wire:
            coords = coords_from_segment(seg, curr_coord, wire_num, step)
            for coord in coords:
                if (coord.x, coord.y) in coord_dict.keys():
                    coord_dict[(coord.x, coord.y)].wire_flags |= coord.wire_flags
                    coord_dict[(coord.x, coord.y)].steps[wire_num] = coord.steps[wire_num]
                else:
                    coord_dict[(coord.x, coord.y)] = coord
            curr_coord = coords[-1]
            step = curr_coord.steps[wire_num]

    return [coord_dict[coord] for coord in coord_dict if coord_dict[coord].wire_flags == 3]


def coords_from_segment(seg, start_coord, wire_num, step):
    coords = []
    dist = int(seg[1:])
    if seg[0] == "U":
        for y in range(start_coord.y+1, start_coord.y+dist+1):
            step += 1
            coords.append(Coordinate(start_coord.x, y, wire_num, step))
    elif seg[0] == "D":
        for y in range(start_coord.y-1, start_coord.y-dist-1, -1):
            step += 1
            coords.append(Coordinate(start_coord.x, y, wire_num, step))
    elif seg[0] == "R":
        for x in range(start_coord.x+1, start_coord.x+dist+1):
            step += 1
            coords.append(Coordinate(x, start_coord.y, wire_num, step))
    elif seg[0] == "L":
        for x in range(start_coord.x-1, start_coord.x-dist-1, -1):
            step += 1
            coords.append(Coordinate(x, start_coord.y, wire_num, step))
    return coords


def main():
    puzzle_input = adventofcode.read_input(3)
    wire1, wire2 = puzzle_input[0].split(','), puzzle_input[1].split(',')
    adventofcode.answer(1, 709, intersect_distance(wire1, wire2))
    adventofcode.answer(2, 13836, intersect_min_steps(wire1, wire2))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
