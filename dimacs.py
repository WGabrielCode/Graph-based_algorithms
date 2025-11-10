import os


class Graph:
    def __init__(self, dir, fileName):
        self.directory = dir
        self.fileName = fileName
        self.filePath = os.path.join(dir, fileName)

        self.A = None
        self.V = None
        self.L = None
        self.S = None

    def loadCNFFormula(self):

        V = 0
        L = []

        f = open(self.filePath, "r")
        lines = f.readlines()
        for l in lines:
            s = l.split()
            if (len(s) < 1): continue
            if (s[0] == "c"):
                print(s)
                continue
            elif (s[0] == "p"):
                V = int(s[2])
            else:
                clause = [int(v)-1 for v in s[:-1]]
                L.append(clause)

        f.close()

        self.solutionLoad()
        self.V = V
        self.L = L

    def loadWeightedGraph(self):
        V = 0
        L = []

        f = open(self.filePath, "r")
        lines = f.readlines()
        for l in lines:
            s = l.split()
            if (len(s) < 1): continue
            if (s[0] == "c"):
                continue
            elif (s[0] == "p"):
                V = int(s[2])
            elif (s[0] == "e"):
                (a, b, c) = (int(s[1]), int(s[2]), int(s[3]))
                (x, y, c) = (min(a, b), max(a, b), c)
                L.append((x-1, y-1, c))
        f.close()
        self.solutionLoad()
        self.V = V
        self.L = L
        A = [[] for _ in range(self.V)]
        for (u, v, w) in self.L:
            A[u].append((v, w))
            A[v].append((u, w))
        self.A = A

    def loadDirectedWeightedGraph(self):

        V = 0
        L = []

        f = open(self.filePath, "r")
        lines = f.readlines()
        for l in lines:
            s = l.split()
            if (len(s) < 1): continue
            if (s[0] == "c"):
                continue
            elif (s[0] == "p"):
                V = int(s[2])
            elif (s[0] == "e"):
                (a, b, c) = (int(s[1]), int(s[2]), int(s[3]))
                L.append((a-1, b-1, c))
        f.close()
        self.V = V
        self.L = L
        self.solutionLoad()
        A = [[] for _ in range(self.V)]
        for (u, v, w) in self.L:
            A[u].append((v, w))
        self.A = A

    def solutionLoad(self):
        with open(self.filePath, 'r') as f:
            line = f.readline()
            self.S = line.split()[-1]
