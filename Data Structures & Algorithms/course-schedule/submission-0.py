class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # course -> preques
        mapCP = { i: [] for i in range( numCourses ) }
        for c, p in prerequisites:
            mapCP[c].append( p )
        
        visited = set()

        def dfs( c ):
            if c in visited:
                return False
            if not mapCP[c]:
                return True

            visited.add( c )
            for p in mapCP[c]:
                if not dfs( p ):
                    return False
            
            visited.remove( c )
            return True
        
        for c in range( numCourses ):
            if not dfs( c ):
                return False

        return True