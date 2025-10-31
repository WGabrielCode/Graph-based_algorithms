import dimacs

def Solution( V , E , s , t ) :
    def E_to_AdjList() :
        minWeight = float("inf")
        maxWeight = 0
        for u , v , weight in E :

            minWeight = min( minWeight , weight )
            maxWeight = max( maxWeight , weight )
            u , v = u-1 , v-1
            A[u].append( ( v , weight ) )
            A[v].append( ( u , weight )  )
        return minWeight , maxWeight

    def dfs( u , condition ) :
        if u == t :
            return True

        visited[u] = True
        for v , weight in A[u] :
            if not visited[v] and weight >= condition :
                if dfs( v , condition ) :
                    return True
        return False

    A = [ [] for _ in range( V ) ]

    result = 0

    left , right  = E_to_AdjList()
    while left <= right :
        mid = ( left + right ) // 2
        visited = [False] * V
        if dfs( s , mid ) :
            result = mid
            left = mid + 1
        else :
            right = mid - 1

    return result

fileName = "grid5x5"
dirPath = "Graphs/"
filePath = dirPath + fileName

S = dimacs.readSolution( filePath )
V , E = dimacs.loadWeightedGraph( filePath )
s , t = 0 , 1
print( Solution( V , E , s , t  ) )
print( S )