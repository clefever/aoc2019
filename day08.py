import adventofcode


def part1(puzzle_input):
    num_layers = len(puzzle_input) // (6*25)
    layers = [{} for i in range(num_layers)]
    counter = 0
    for layer in range(num_layers):
        for y in range(6):
            for x in range(25):
                layers[layer][(x,y)] = int(puzzle_input[counter])
                counter += 1
    min_zeros = 99999999
    min_zeros_layer = -1
    for layer in range(len(layers)):
        zeros = sum([layers[layer][pixel] == 0 for pixel in layers[layer].keys()])
        if zeros < min_zeros:
            min_zeros = zeros
            min_zeros_layer = layer
    
    num_ones, num_twos = 0, 0
    for pixel in layers[min_zeros_layer].keys():
        if layers[min_zeros_layer][pixel] == 1:
            num_ones += 1
        if layers[min_zeros_layer][pixel] == 2:
            num_twos += 1
    return num_twos * num_ones


def part2(puzzle_input):
    layer_counter = len(puzzle_input) // (6*25)
    layers = [{} for i in range(layer_counter)]
    counter = 0
    for layer in range(layer_counter):
        for y in range(6):
            for x in range(25):
                layers[layer][(x,y)] = int(puzzle_input[counter])
                counter += 1
    final_image = {}
    for y in range(6):
        for x in range(25):
            final_image[(x,y)] = 2
    counter = 0
    for layer in range(layer_counter):
        for y in range(6):
            for x in range(25):
                if final_image[(x,y)] == 2:
                    final_image[(x,y)] = int(puzzle_input[counter])
                counter += 1
    for y in range(6):
        for x in range(25):
            if final_image[(x,y)] == 0:
                print(" ", end = " ")
            else:
                print("X", end = " ")
        print()


def main():
    puzzle_input = adventofcode.read_input(8)
    adventofcode.answer(1, 1572, part1(puzzle_input))
    adventofcode.answer(2, 0, part2(puzzle_input))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
