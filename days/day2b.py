import fileinput

inputfile = "inputfiles/day2_input.txt"


class Position:
    def __init__(self, x=0, y=0, aim=0):
        self.x = x
        self.y = y
        self.aim = aim

    def forward(self, value):
        self.x += int(value)
        self.y += self.aim * int(value)

    def down(self, value):
        self.aim += int(value)

    def up(self, value):
        self.aim -= int(value)


def pilot():
    position = Position()
    for line in fileinput.input(inputfile):
        command, sep, value = line.rstrip().partition(' ')
        if command == 'forward':
            position.forward(value)
        elif command == 'down':
            position.down(value)
        elif command == 'up':
            position.up(value)
        else:
            print('Unknown command "{}" in line {}'.format(line.rstrip(),  fileinput.filelineno()))
            exit(1)
    return position


position = pilot()
print('position: {}/{}  product: {}'.format(position.x, position.y, position.x * position.y))
