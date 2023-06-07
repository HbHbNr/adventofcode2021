from typing import List


class Graph:

    def __init__(self, lines: List[str]) -> None:
        self._vertices = {}
        for line in lines:
            vs = line.split('-')
            self.addPath(vs[0], vs[1])
            self.addPath(vs[1], vs[0])

    def addPath(self, fromvertex, tovertex) -> None:
        if not fromvertex in self._vertices:
            self._vertices[fromvertex] = { tovertex }
        else:
            self._vertices[fromvertex].add(tovertex)

    def findDistinctPaths(self) -> List[List[str]]:
        distinctPaths = []
        self.traverse(distinctPaths, 'start', [])
        return distinctPaths

    def traverse(self, distinctPaths, currentpos, currentpath) -> None:
        newpath = list(currentpath)
        newpath.append(currentpos)
        if currentpos == 'end':
            print(newpath)
            distinctPaths.append(newpath)
        else:
            targets = self._vertices[currentpos]
            for target in targets:
                if Graph.isBigCave(target):
                    self.traverse(distinctPaths, target, newpath)  # visit big caves any number of times
                elif not target in currentpath:
                    self.traverse(distinctPaths, target, newpath)  # visit small caves at most once
                else:
                    pass  # would be more than one visit to a small cave

    @classmethod
    def isBigCave(cls, vertex):
        return vertex == vertex.upper()

    def __str__(self):
        return ','.join(self._vertices.keys())


if __name__ == '__main__':
    from days import util

    # lines = util.readinputfile('inputfiles/day12_example1.txt')
    lines = util.readinputfile('inputfiles/day12_input.txt')
    graph = Graph(lines)
    print(graph)
    paths = graph.findDistinctPaths()

    print('DAY12A - Number of distinct paths: ' + str(len(paths)))
