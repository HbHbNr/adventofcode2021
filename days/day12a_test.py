from util import util
from days import day12a


def testExample1():
    lines = util.readinputfile('inputfiles/day12_example1.txt')
    graph = day12a.Graph(lines)
    paths = graph.findDistinctPaths()

    assert len(paths) == 10

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


def testExample2():
    lines = util.readinputfile('inputfiles/day12_example2.txt')
    graph = day12a.Graph(lines)
    paths = graph.findDistinctPaths()

    assert len(paths) == 19


def testExample3():
    lines = util.readinputfile('inputfiles/day12_example3.txt')
    graph = day12a.Graph(lines)
    paths = graph.findDistinctPaths()

    assert len(paths) == 226


def testInput():
    lines = util.readinputfile('inputfiles/day12_input.txt')
    graph = day12a.Graph(lines)
    paths = graph.findDistinctPaths()

    assert len(paths) == 4378
