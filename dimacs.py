import os

class Graph :
    def __init__( self , dir , fileName ) :
        self.directory = dir
        self.fileName = fileName
        self.filePath = os.path.join( dir , fileName )

        self.V = None
        self.A = None
        self.S = None

    def loadCNFFormula( self ):

      V = 0
      L = []

      f = open( self.filePath, "r" )
      lines = f.readlines()
      for l in lines:
        s = l.split()
        if(len(s) < 1): continue
        if( s[0] == "c" ):
          print(s)
          continue
        elif( s[0] == "p" ):
          V = int(s[2])
        else:
          clause = [int(v) for v in s[:-1]]
          L.append(clause)

      f.close()

      self.solutionLoad()
      self.V = V
      self.L = L
      return (V,L)



    def loadWeightedGraph( self ):
      V = 0
      L = []

      f = open( self.filePath, "r" )
      lines = f.readlines()
      for l in lines:
        s = l.split()
        if(len(s) < 1): continue
        if( s[0] == "c" ):
          continue
        elif( s[0] == "p" ):
          V = int(s[2])
        elif( s[0] == "e" ):
          (a,b,c) = (int(s[1]), int(s[2]), int(s[3]))
          (x,y,c) = (min(a,b), max(a,b), c)
          L.append((x,y,c))

      f.close()

      self.solutionLoad()
      self.V = V
      self.L = L
      return (V,L)



    def loadDirectedWeightedGraph(self):

      V = 0
      L = []

      f = open( self.filePath , "r")
      lines = f.readlines()
      for l in lines:
        s = l.split()
        if(len(s) < 1): continue
        if( s[0] == "c" ):
          continue
        elif( s[0] == "p" ):
          V = int(s[2])
        elif( s[0] == "e" ):
          (a,b,c) = (int(s[1]), int(s[2]), int(s[3]))
          L.append((a,b,c))

      f.close()

      self.solutionLoad()
      self.V = V
      self.L = L
      return (V,L)


    def solutionLoad(self):
        with open(self.filePath, 'r') as f:
            line = f.readline()
            self.S = line.split()[-1]

