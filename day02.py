import re

def possibleGame(game):
    nr = int(re.match(r'Game (\d*)', game).group(1))
    return nr if max([int(cubes) for cubes in re.findall(r'(\d*) red', game)]) <= 12 and \
            max([int(cubes) for cubes in re.findall(r'(\d*) green', game)]) <= 13 and \
            max([int(cubes) for cubes in re.findall(r'(\d*) blue', game)]) <= 14 \
        else 0

def possibleCubeAmount(game):
    return max([int(cubes) for cubes in re.findall(r'(\d*) red', game)]) * \
        max([int(cubes) for cubes in re.findall(r'(\d*) green', game)]) * \
        max([int(cubes) for cubes in re.findall(r'(\d*) blue', game)])

print('part1:', sum([possibleGame(line) for line in open('inputs/day02.txt')]))
print('part2:', sum([possibleCubeAmount(line) for line in open('inputs/day02.txt')]))
