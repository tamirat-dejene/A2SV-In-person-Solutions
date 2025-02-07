class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
    #   ball: color, color: n_ball(s)
        ball_color, color_cnt = {}, {}
    #   current unique colors, returned value
        unique_cnt, ans = 0, []

        for [b, c] in queries:
            if b in ball_color:
                old_color = ball_color[b]
                color_cnt[old_color] -= 1

                if color_cnt[old_color] == 0: 
                    del color_cnt[old_color]
                    unique_cnt -= 1 
                
            if c in color_cnt: unique_cnt -= 1
                
            ball_color[b] = c
            color_cnt[c] = color_cnt.get(c, 0) + 1
            unique_cnt += 1
            ans.append(unique_cnt)

        return ans