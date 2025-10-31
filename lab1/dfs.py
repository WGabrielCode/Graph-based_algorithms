import dimacs
from lab1.dimacs import readSolution


def Solution( V , E , s , t ) :

    def E_to_AdjList() :
        for u , v , weight in E :
            u , v = u-1 , v-1
            A[u].append( ( v , weight ) )
            A[v].append( ( u , weight )  )

    def dfs( u , minWeight ):
        visited[u] = True
        for v , weight in A[u] :
            if not visited[v] :
                newMinWeight = min( minWeight , weight )
                if v == t :
                    nonlocal result
                    result = max( result , newMinWeight )
                else :
                    dfs( v , newMinWeight )
                    visited[v] = False


    A = [ [] for _ in range( V ) ]
    E_to_AdjList()
    visited = [ False ] * V
    result = 0
    dfs( s , float("inf")  )

    return result


fileName = "grid5x5"
V , E = dimacs.loadDirectedWeightedGraph( "Graphs/" + fileName )
S = dimacs.readSolution( "Graphs/" + fileName )
s , t = 0 , 1

print( Solution( V , E , s , t  ) )
print( S )