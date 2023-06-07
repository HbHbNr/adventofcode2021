from days import util, day12b


def test_example1():
    lines = util.readinputfile('inputfiles/day12_example1.txt')
    graph = day12b.Graph(lines)
    paths = graph.findDistinctPaths()

    assert len(paths) == 36

    # start,A,b,A,c,A,end
    # start,A,b,A,end
    # start,A,b,end
    # start,A,c,A,b,A,end
    # start,A,c,A,b,end
    # start,A,c,A,end
    # start,A,end
    # start,b,A,c,A,end
    # start,b,A,end
    # start,b,end
    assert ['start', 'A', 'b', 'A', 'c', 'A', 'end'] in paths
    assert ['start', 'A', 'b', 'end'] in paths
    assert ['start', 'b', 'end'] in paths
    assert ['start', 'A', 'b', 'A', 'b', 'A', 'c', 'A', 'end'] in paths
    assert ['start', 'A', 'c', 'A', 'b', 'd', 'b', 'A', 'end'] in paths
    assert ['start', 'b', 'd', 'b', 'A', 'c', 'A', 'end'] in paths


def test_example2():
    lines = util.readinputfile('inputfiles/day12_example2.txt')
    graph = day12b.Graph(lines)
    paths = graph.findDistinctPaths()

    assert len(paths) == 103


def test_example3():
    lines = util.readinputfile('inputfiles/day12_example3.txt')
    graph = day12b.Graph(lines)
    paths = graph.findDistinctPaths()

    assert len(paths) == 3509


def test_input():
    lines = util.readinputfile('inputfiles/day12_input.txt')
    graph = day12b.Graph(lines)
    paths = graph.findDistinctPaths()

    assert len(paths) == 133621
