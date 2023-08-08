"""Solution for https://adventofcode.com/2021/day/18 part b"""
import itertools
from days import day18a
from util import util


def main():
    magnitudes = []
    # tokenListList = day18a.MathHomework.readTokenFile('inputfiles/day18_example2.txt')
    tokenListList = day18a.MathHomework.readTokenFile('inputfiles/day18_input.txt')
    for pair in itertools.permutations(tokenListList, 2):
        tokenList = day18a.MathHomework.addAndReduce(pair)
        magnitude = day18a.MathHomework.calcMagnitude(token for token in tokenList)
        magnitudes.append(magnitude)

    util.printresultline('18b', max(magnitudes))


if __name__ == '__main__':
    main()
