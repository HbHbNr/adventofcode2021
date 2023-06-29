if __name__ == '__main__':
    from days import util

    bs: bytes = util.readhexinputfile('inputfiles/day16_example1.txt')
    # util.readhexinputfile('inputfiles/day16_input.txt')
    for i in range(len(bs)):
        print(bs[i], bin(bs[i]))
