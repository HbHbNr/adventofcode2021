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
        # visit small caves at most twice
        valid = False
        if Graph.isBigCave(target):
            valid = True
        elif target == 'start':
            valid = False
        elif target not in newpath:
            valid = True
        else:
            valid = not Graph.anySmallCaveContainedTwice(newpath)
        return valid

    @classmethod
    def isBigCave(cls, vertex: str) -> bool:
        return vertex == vertex.upper()

    @classmethod
    def anySmallCaveContainedTwice(cls, currentpath: List[str]) -> bool:
        smallcaves = [cave for cave in currentpath if not Graph.isBigCave(cave)]
        uniquesmallcaves = set(smallcaves)
        for cave in uniquesmallcaves:
            if smallcaves.count(cave) > 1:
                return True
        return False

    def __str__(self):
        return ','.join(self._vertices.keys())


if __name__ == '__main__':
    from days import util

    # lines = util.readinputfile('inputfiles/day12_example1.txt')
    lines = util.readinputfile('inputfiles/day12_input.txt')
    graph = Graph(lines)
    # print(graph)
    paths = graph.findDistinctPaths()

    print('DAY12B - Number of distinct paths: ' + str(len(paths)))
