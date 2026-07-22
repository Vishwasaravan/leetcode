class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def is_in_bounds(r, c, dr):
            # Special case: The top row of a ring is filled first.
            # When moving UP (dr == -1), the ceiling shifts down by 1 to prevent overshoot.
            top_bound = layer + 1 if dr == -1 else layer
            return (top_bound <= r < m - layer) and (layer <= c < n - layer)

        layer = 0
        # Cyclical directions: Right -> Down -> Left -> Up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0
        i = j = 0
        
        m = len(matrix)
        n = len(matrix[0])
        mat_len = m * n
        res = []

        # Iterate exactly for the total number of elements in the grid
        for _ in range(mat_len):
            res.append(matrix[i][j])
            dr, dc = directions[curr_dir]
            
            # Look ahead to see if the next step collides with the current ring boundary
            if not is_in_bounds(i + dr, j + dc, dr):
                # If we were moving UP and hit a wall, the current layer ring is finished
                if directions[curr_dir] == (-1, 0):
                    layer += 1 # Shrink boundaries inward for the next ring
                
                # Cycle cleanly to the next direction
                curr_dir = (curr_dir + 1) % 4
                dr, dc = directions[curr_dir]
            
            # Step forward
            i += dr
            j += dc

        return res
 
        
        