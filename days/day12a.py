from typing import List, Dict, Set


class Graph:

    def __init__(self, lines: List[str]) -> None:
        self._vertices: Dict[str, Set[str]] = {}
        for line in lines:
            vs = line.split('-')
            self.addPath(vs[0], vs[1])
            self.addPath(vs[1], vs[0])

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
        newpath = list(currentpath)
        newpath.append(currentpos)
        if currentpos == 'end':
            # print(','.join(newpath))
            distinctPaths.append(newpath)
        else:
            targets = self._vertices[currentpos]
            for target in targets:
                if Graph.isValidTarget(newpath, target):
                    self.traverse(distinctPaths, target, newpath)
                # ignore invalid targets

    @classmethod
    def isValidTarget(cls, newpath: List[str], target: str) -> bool:
        # visit big caves any number of times
        # visit small caves at most once
        return Graph.isBigCave(target) or target not in newpath

    @classmethod
    def isBigCave(cls, vertex: str) -> bool:
        return vertex == vertex.upper()

    def __str__(self):
        return ','.join(self._vertices.keys())


def main():
    from util import util

    # lines = util.readinputfile('inputfiles/day12_example1.txt')
    lines = util.readinputfile('inputfiles/day12_input.txt')
    graph = Graph(lines)
    # print(graph)
    paths = graph.findDistinctPaths()

    print('DAY12A - Number of distinct paths: ' + str(len(paths)))


if __name__ == '__main__':
    main()
