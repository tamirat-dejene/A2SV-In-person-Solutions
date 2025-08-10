class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []

        for a, b in queries:
            # find common parent (closest)
            pa, pb = a, b

            path_a = set([a])
            path_b = set([b])

            while (pa != pb) and pa not in path_b and pb not in path_a:
                pa, pb = max(1, pa), max(1, pb)
                
                # find depth
                da = floor(log2(pa)) 
                db = floor(log2(pb))

                # find lb for each row
                lb_a = 1 << da
                lb_b = 1 << db

                # find lb for new parent
                lb_pa = lb_a >> 1
                lb_pb = lb_b >> 1

                # calc new parent
                pa = lb_pa + (pa - lb_a) // 2
                pb = lb_pb + (pb - lb_b) // 2

                path_a.add(pa)
                path_b.add(pb)
            
            if pa in path_b:
                pb = pa
            elif pb in path_a:
                pa = pb
            elif pa != pb:
                pa, pb = 1, 1
            
            pa, pb = max(1, pa), max(1, pb)

            da = floor(log2(a)) - floor(log2(pa))
            db = floor(log2(b)) - floor(log2(pb))
            
            res.append(da + db + 1)
        
        return res
        