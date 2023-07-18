from days import day3a


def testInput():
    # inputfile = "inputfiles/day3_example.txt"
    inputfile = "inputfiles/day3_input.txt"

    histogram = day3a.createhistogram(inputfile)
    gamma = histogram.buildparameter(True)
    epsilon = histogram.buildparameter(False)

    assert int(gamma, 2) * int(epsilon, 2) == 738234
