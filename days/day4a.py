class BingoBoard:
    def __init__(self, rows):
        self.rows = [row.split(None) for row in rows]
        self.columns = [[] for x in range(5)]
        for index, column in enumerate(self.columns):
            for row in self.rows:
                column.append(row[index])

    def print(self):
        for row in self.rows:
            print('{:>2} {:>2} {:>2} {:>2} {:>2}'.format(*row))

    def play(self, pickednumbers):
        for index, pickednumber in enumerate(pickednumbers):
            print(pickednumber)
            for row_or_column in [*self.rows, *self.columns]:
                if pickednumber in row_or_column:
                    print(f'{pickednumber} found in {row_or_column}')


class BingoMatch:
    def __init__(self, lines):
        self.pickednumbers = lines[0].split(',')
        self.bingoboards = []
        index = 2
        while index < len(lines):
            bingoboard = BingoBoard(lines[index:index+5])
            self.bingoboards.append(bingoboard)
            index += 6

    def play(self):
        for bingoboard in self.bingoboards:
            bingoboard.play(['22'])
            # bingoboard.play(['7', '4', '9', '5', '11', '17'])
            # bingoboard.play(self.pickednumbers)


if __name__ == '__main__':
    import util

    lines = util.readinputfile('inputfiles/day4_example.txt')
    # lines = util.readinputfile('inputfiles/day4_input.txt')
    bingomatch = BingoMatch(lines)
    for bingoboard in bingomatch.bingoboards:
        bingoboard.print()
        print()
    bingomatch.play()
#    print('oxygen: {} -> {}'.format(oxygen, int(oxygen, 2)))
#    print('co2: {} -> {}'.format(co2, int(co2, 2)))
#    print('oxygen * co2: {}'.format(int(oxygen, 2) * int(co2, 2)))
