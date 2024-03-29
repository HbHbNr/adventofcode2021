"""Solution for https://adventofcode.com/2021/day/12 part b"""
from typing import List, Dict, Set
from util import util


class Graph:

    def __init__(self, lines: List[str]) -> None:
        self._vertices: Dict[str, Set[str]] = {}
        for line in lines:
            vertices = line.split('-')
            self.addPath(vertices[0], vertices[1])
            self.addPath(vertices[1], vertices[0])
        caves = self._vertices.keys()
        self._bigcaves = [cave for cave in caves if Graph.isBigCave(cave)]
        self._smallcaves = [cave for cave in caves if not Graph.isBigCave(cave)]

    def addPath(self, fromvertex: str, tovertex: str) -> None:
        if fromvertex not in self._vertices:
            self._vertices[fromvertex] = {tovertex}
        else:
            self._vertices[fromvertex].add(tovertex)

    def findDistinctPaths(self) -> List[List[str]]:
        distinctPaths: List[List[str]] = []
        self.traverse(distinctPaths, 'start', [])  # start traversal
        return distinctPaths

    def traverse(self, distinctPaths: List[List[str]], currentpos: str, currentpath: List[str]) -> None:
        currentpath.append(currentpos)
        if currentpos == 'end':
            # print(','.join(currentpath))
            distinctPaths.append(list(currentpath))
        else:
            targets = self._vertices[currentpos]
            for target in targets:
                if self.isValidTarget(currentpath, target):
                    self.traverse(distinctPaths, target, currentpath)
                # ignore invalid targets
        currentpath.pop()

    def isValidTarget(self, newpath: List[str], target: str) -> bool:
        # visit big caves any number of times
        # visit small caves at most twice
        valid = False
        if target in self._bigcaves:
            valid = True
        elif target == 'start':
            valid = False
        elif target not in newpath:
            valid = True
        else:
            valid = not self.anySmallCaveContainedTwice(newpath)
        return valid

    def anySmallCaveContainedTwice(self, currentpath: List[str]) -> bool:
        for cave in self._smallcaves:
            if currentpath.count(cave) > 1:
                return True
        return False

    @classmethod
    def isBigCave(cls, vertex: str) -> bool:
        return vertex == vertex.upper()

    def __str__(self):
        return ','.join(self._vertices.keys())


def main():
    # lines = util.readinputfile('inputfiles/day12_example1.txt')
    lines = util.readinputfile('inputfiles/day12_input.txt')
    graph = Graph(lines)
    # print(graph)
    paths = graph.findDistinctPaths()

    util.printresultline('12b', len(paths))


if __name__ == '__main__':
    main()
