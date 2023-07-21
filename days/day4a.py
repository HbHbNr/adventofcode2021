class BingoBoard:
    def __init__(self, rows):
        self._rows = [[int(x) for x in row.split(None)] for row in rows]
        self._columns = [[] for x in range(5)]
        for index, column in enumerate(self._columns):
            for row in self._rows:
                column.append(row[index])

    def print(self, indent=''):
        for row in self._rows:
            print('{}{:2} {:2} {:2} {:2} {:2}'.format(indent, *row))  # pylint: disable=consider-using-f-string

    def playNumber(self, pickednumber):
        for rowOrColumn in [*self._rows, *self._columns]:
            if pickednumber in rowOrColumn:
                # print(f'{pickednumber} found in {row_or_column}')
                rowOrColumn[rowOrColumn.index(pickednumber)] = -1

    def sum(self):
        result = 0
        for row in self._rows:
            for number in row:
                result += number if number != -1 else 0
        return result

    def isWinner(self):
        result = self._rows.count([-1, -1, -1, -1, -1]) > 0 or self._columns.count([-1, -1, -1, -1, -1]) > 0
        return result

    # for unit testing
    def getRow(self, rowIndex):
        return tuple(self._rows[rowIndex])

    # for unit testing
    def getColumn(self, columnIndex):
        return tuple(self._columns[columnIndex])


class BingoMatch:
    # pylint: disable=too-few-public-methods

    def __init__(self, lines):
        self._pickednumbers = [int(x) for x in lines[0].split(',')]
        self._bingoboards = []
        index = 2
        while index < len(lines):
            bingoboard = BingoBoard(lines[index:index+5])
            self._bingoboards.append(bingoboard)
            index += 6

    def play(self):
        pickednumbers = self._pickednumbers
        for numberindex, pickednumber in enumerate(pickednumbers):
            for boardindex, bingoboard in enumerate(self._bingoboards):
                # print(pickednumber)
                # print(bingoboard.sum())
                bingoboard.playNumber(pickednumber)
                # print(bingoboard.sum())
                if bingoboard.isWinner():
                    # print(f'Winning board, numberindex {numberindex}, boardindex {boardindex}:')
                    # bingoboard.print('  ')
                    boardsum = bingoboard.sum()
                    return {'numberindex': numberindex, 'pickednumber': pickednumber, 'boardindex': boardindex,
                            'boardsum': boardsum, 'solution': pickednumber * boardsum}
        return None


def main():
    from util import util

    lines = util.readinputfile('inputfiles/day4_input.txt')
    bingomatch = BingoMatch(lines)
    result = bingomatch.play()
    print(result)
    if result is not None:
        print(result['pickednumber'] * result['boardsum'])


if __name__ == '__main__':
    main()
