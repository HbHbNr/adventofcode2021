from days import day3b


def test_determineratings():
    oxygen, co2 = day3b.determineratings('inputfiles/day3_example.txt')
    assert oxygen == '10111'
    assert co2 == '01010'
