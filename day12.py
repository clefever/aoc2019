import math
import adventofcode


class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.x_start = x
        self.y_start = y
        self.z_start = z
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.x_step = -1
        self.y_step = -1
        self.z_step = -1
        self.steps = 0
        self.x_half = -1
        self.y_half = -1
        self.z_half = -1

    def apply_gravity(self, moons):
        others = [m for m in moons if m != self]
        for moon in others:
            if self.x < moon.x:
                self.vx += 1
            elif self.x > moon.x:
                self.vx -= 1
            if self.y < moon.y:
                self.vy += 1
            elif self.y > moon.y:
                self.vy -= 1
            if self.z < moon.z:
                self.vz += 1
            elif self.z > moon.z:
                self.vz -= 1

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        self.steps += 1
        self.apply_history()

    def apply_history(self):
        if self.x_start == self.x and self.vx == 0:
            if self.x_half == -1:
                self.x_half = self.steps
            else:
                if self.steps == self.x_half * 2:
                    self.x_step = self.steps // 2
                else:
                    self.x_half = self.steps
        if self.y_start == self.y and self.vy == 0:
            if self.y_half == -1:
                self.y_half = self.steps
            else:
                if self.steps == self.y_half * 2:
                    self.y_step = self.steps // 2
                else:
                    self.y_half = self.steps
        if self.z_start == self.z and self.vz == 0:
            if self.z_half == -1:
                self.z_half = self.steps
            else:
                if self.steps == self.z_half * 2:
                    self.z_step = self.steps // 2
                else:
                    self.z_half = self.steps

    def total_energy(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) * (abs(self.vx) + abs(self.vy) + abs(self.vz))

    def has_cycles(self):
        return self.x_step != -1 and self.y_step != -1 and self.z_step != -1

    def cycle_value(self):
        return lcm(self.x_step, self.y_step, self.z_step)

    def __repr__(self):
        return f"pos=<x={self.x:>3}, y={self.y:>3}, z={self.z:>3}>, vel=<x={self.vx:>3}, y={self.vy:>3}, z={self.vz:>3}>"


def part1(moons, steps):
    """
    >>> part1([Moon(-1, 0, 2), Moon(2, -10, -7), Moon(4, -8, 8), Moon(3, 5, -1)], 10)
    179
    """
    for s in range(steps):
        #print(f"{moons[2]} - Step {s}")
        for moon in moons:
            moon.apply_gravity(moons)
        for moon in moons:
            moon.apply_velocity()
    return sum(moon.total_energy() for moon in moons)


def part2(moons):
    """
    >>> part2([Moon(-1, 0, 2), Moon(2, -10, -7), Moon(4, -8, 8), Moon(3, 5, -1)])
    2772
    """
    have_cycles = {}
    while True:
        for moon in moons:
            moon.apply_gravity(moons)
        for moon in moons:
            moon.apply_velocity()
            #moon.apply_history()
            # if len(moons[0].x_hist) % 100000 == 0:
            #     print(len(moons[0].x_hist))
            if moon not in have_cycles and moon.has_cycles():
                have_cycles[moon] = moon.cycle_value()
        #         print("found a cycle")
        if len(have_cycles) == 4:
            m = list(have_cycles.values())
            return lcm(m[0], m[1], m[2], m[3])
    # steps = 0
    # while True:
    #     steps += 1
    #     curr = [moons[0].x, moons[0].y, moons[0].z, moons[0].vx, moons[0].vy, moons[0].vz,
    #             moons[1].x, moons[1].y, moons[1].z, moons[1].vx, moons[1].vy, moons[1].vz,
    #             moons[2].x, moons[2].y, moons[2].z, moons[2].vx, moons[2].vy, moons[2].vz,
    #             moons[3].x, moons[3].y, moons[3].z, moons[3].vx, moons[3].vy, moons[3].vz,
    #             ]
    #     for moon in moons:
    #         others = [m for m in moons if m != moon]
    #         moon.apply_gravity(others)
    #     for moon in moons:
    #         others = [m for m in moons if m != moon]
    #         moon.apply_velocity()
    #     after = [moons[0].x, moons[0].y, moons[0].z, moons[0].vx, moons[0].vy, moons[0].vz,
    #              moons[1].x, moons[1].y, moons[1].z, moons[1].vx, moons[1].vy, moons[1].vz,
    #              moons[2].x, moons[2].y, moons[2].z, moons[2].vx, moons[2].vy, moons[2].vz,
    #              moons[3].x, moons[3].y, moons[3].z, moons[3].vx, moons[3].vy, moons[3].vz,
    #              ]
    #     [print(m.accels()) for m in moons]
    #     print("------")
    #     if curr == after:
    #         return steps


def lcm(a, b, c = 1, d = 1):
    first = abs(a*b) // math.gcd(a, b)
    second = abs(first*c) // math.gcd(first, c)
    return abs(second*d) // math.gcd(second, d)


def main():
    #puzzle_input = adventofcode.read_input(12)
    # <x=14, y=9, z=14>
    # <x=9, y=11, z=6>
    # <x=-6, y=14, z=-4>
    # <x=4, y=-4, z=-3>

    moon1 = Moon(14, 9, 14)
    moon2 = Moon(9, 11, 6)
    moon3 = Moon(-6, 14, -4)
    moon4 = Moon(4, -4, -3)
    adventofcode.answer(1, 9999, part1([moon1, moon2, moon3, moon4], 1000))
    #adventofcode.answer(2, 0, part2([moon1, moon2, moon3, moon4]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
