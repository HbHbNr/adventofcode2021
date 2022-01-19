class BingoBoard:
    def __init__(self, rows):
        self.rows = [[int(x) for x in row.split(None)] for row in rows]
        self.columns = [[] for x in range(5)]
        for index, column in enumerate(self.columns):
            for row in self.rows:
                column.append(row[index])

    def print(self):
        for row in self.rows:
            print('{:2} {:2} {:2} {:2} {:2}'.format(*row))

    def playNumber(self, pickednumber):
        for row_or_column in [*self.rows, *self.columns]:
            if pickednumber in row_or_column:
                # print(f'{pickednumber} found in {row_or_column}')
                row_or_column[row_or_column.index(pickednumber)] = -1

    def sum(self):
        result = 0
        for row in self.rows:
            for number in row:
                result += number if number != -1 else 0
        return result

    def isWinner(self):
        result = self.rows.count([-1, -1, -1, -1, -1]) > 0 or self.columns.count([-1, -1, -1, -1, -1]) > 0
        return result


class BingoMatch:
    def __init__(self, lines):
        self.pickednumbers = [int(x) for x in lines[0].split(',')]
        self.bingoboards = []
        index = 2
        while index < len(lines):
            bingoboard = BingoBoard(lines[index:index+5])
            self.bingoboards.append(bingoboard)
            index += 6

    def play(self):
        # pickednumbers = [22]
        # pickednumbers = [7, 4, 9, 5, 11, 17]
        pickednumbers = self.pickednumbers
        for numberindex, pickednumber in enumerate(pickednumbers):
            for boardindex, bingoboard in enumerate(self.bingoboards):
                # print(pickednumber)
                # print(bingoboard.sum())
                bingoboard.playNumber(pickednumber)
                # print(bingoboard.sum())
                if bingoboard.isWinner():
                    print(f'Winning board, numberindex {numberindex}, boardindex {boardindex}:')
                    bingoboard.print()
                    return {'numberindex': numberindex, 'pickednumber': pickednumber, 'boardindex': boardindex, 'boardsum': bingoboard.sum()}
        return None

if __name__ == '__main__':
    import util

    # lines = util.readinputfile('inputfiles/day4_example.txt')
    lines = util.readinputfile('inputfiles/day4_input.txt')
    bingomatch = BingoMatch(lines)
    #for bingoboard in bingomatch.bingoboards:
    #    bingoboard.print()
    #    print()
    result = bingomatch.play()
    print(result)
    if result is not None:
        print(result['pickednumber'] * result['boardsum'])
    #for bingoboard in bingomatch.bingoboards:
    #    bingoboard.print()
    #    print()
#    print('oxygen: {} -> {}'.format(oxygen, int(oxygen, 2)))
#    print('co2: {} -> {}'.format(co2, int(co2, 2)))
#    print('oxygen * co2: {}'.format(int(oxygen, 2) * int(co2, 2)))
