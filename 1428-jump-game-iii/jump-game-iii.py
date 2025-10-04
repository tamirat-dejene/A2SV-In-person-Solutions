class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        vis = set([start])
        stack = [start]
        N = len(arr)


        while stack:
            i = stack.pop()
            if arr[i] == 0:
                return True
            n1, n2 = i + arr[i], i - arr[i]

            if 0 <= n1 < N and n1 not in vis:
                vis.add(n1)
                stack.append(n1)
            if 0 <= n2 < N and n2 not in vis:
                vis.add(n2)
                stack.append(n2)

        return False
        