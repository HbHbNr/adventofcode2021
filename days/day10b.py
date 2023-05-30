from typing import List


class Checker:

    _openbrackets = list("([{<")
    _closebrackets = list(")]}>")
    _openbracketsscores = [1, 2, 3, 4]

    def __init__(self, lines: List[str]) -> None:
        self._lines = list(lines)
        return

    def findincompletelines(self) -> List[int]:
        incompletelines = []

        for line in self._lines:
            incompleteline = self.findsyntaxerrorinline(line)
            if incompleteline != []:
                incompletelines.append(incompleteline)

        return incompletelines

    @classmethod
    def findsyntaxerrorinline(self, line) -> int:
        openbrackets = []
        for bracket in list(line):
            if Checker.isopenbracket(bracket):
                openbrackets.append(bracket)
            else:
                lastopenbracket = openbrackets[-1]
                if Checker.matchingbrackets(lastopenbracket, bracket):
                    # closing bracket matches opening bracket
                    openbrackets.pop()
                else:
                    # closing bracket does not match opening bracket
                    return []
        return openbrackets

    @classmethod
    def isopenbracket(cls, bracket):
        return bracket in Checker._openbrackets

    @classmethod
    def matchingbrackets(cls, open, close):
        return Checker._openbrackets.index(open) == Checker._closebrackets.index(close)

    @classmethod
    def calccompletescore(cls, incompletelines) -> int:
        linescores = list(map(Checker.calccompletescoreofline, incompletelines))
        linescores.sort()
        return linescores[len(linescores) // 2]

    @classmethod
    def calccompletescoreofline(cls, incompleteline):
        score = 0
        for bracket in reversed(incompleteline):
            score *= 5
            score += Checker.scoreofbracket(bracket)
        return score

    @classmethod
    def scoreofbracket(cls, bracket):
        return Checker._openbracketsscores[Checker._openbrackets.index(bracket)]


if __name__ == '__main__':
    from days import util

    # lines = util.readinputfile('inputfiles/day10_example.txt')
    lines = util.readinputfile('inputfiles/day10_input.txt')
    checker = Checker(lines)
    incompletelines = checker.findincompletelines()

    # for line in incompletelines:
    #     print(str(line))

    print("Middle score: " + str(Checker.calccompletescore(incompletelines)))
