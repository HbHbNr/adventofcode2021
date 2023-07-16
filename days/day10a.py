from typing import List


class Checker:

    _openbrackets = list("([{<")
    _closebrackets = list(")]}>")
    _closebracketsscores = [3, 57, 1197, 25137]

    def __init__(self, lines: List[str]) -> None:
        self._lines = list(lines)
        return

    def findsyntaxerrors(self) -> List[int]:
        syntaxerrors = []

        for line in self._lines:
            syntaxerror = self.findsyntaxerrorinline(line)
            syntaxerrors.append(syntaxerror)

        return syntaxerrors

    def findsyntaxerrorinline(self, line) -> int:
        openbrackets = []
        for character in list(line):
            if Checker.isopenbracket(character):
                openbrackets.append(character)
            else:
                lastopenbracket = openbrackets[-1]
                if Checker.matchingbrackets(lastopenbracket, character):
                    # closing bracket matches opening bracket
                    openbrackets.pop()
                else:
                    # closing bracket does not match opening bracket
                    return Checker.errorscore(character)
        return 0

    @classmethod
    def isopenbracket(cls, character):
        return character in Checker._openbrackets

    @classmethod
    def matchingbrackets(cls, openBracket, closeBracket):
        return Checker._openbrackets.index(openBracket) == Checker._closebrackets.index(closeBracket)

    @classmethod
    def errorscore(cls, close):
        return Checker._closebracketsscores[Checker._closebrackets.index(close)]


def main():
    from util import util

    # lines = util.readinputfile('inputfiles/day10_example.txt')
    lines = util.readinputfile('inputfiles/day10_input.txt')
    checker = Checker(lines)
    syntaxerrors = checker.findsyntaxerrors()

    # print("syntaxerrors: " + str(syntaxerrors))
    print("syntaxerrorscore: " + str(sum(syntaxerrors)))


if __name__ == '__main__':
    main()
