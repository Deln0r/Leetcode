class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = [] # res[i] = distinct # of colors after queries[i]
        distinct = 0 # current distinct # of colors
        
        ball_color = {} # ball : color of the ball
        color_count = {} # color : count of the color; # of items corresponds to 'distinct'

        for ball, new_color in queries:
            # Considering the removal of the ball's old color, update 'color_count'
            if ball in ball_color:
                old_color = ball_color[ball]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    # A unique color is deleted
                    del color_count[old_color]
                    distinct -= 1

            # Update the ball's color and update 'color_count' as appropriate
            ball_color[ball] = new_color
            if new_color in color_count:
                color_count[new_color] += 1
            else:
                # A unique color is added
                color_count[new_color] = 1
                distinct += 1
            
            # Append the distinct # of colors after executing updates
            res.append(distinct)
        return res