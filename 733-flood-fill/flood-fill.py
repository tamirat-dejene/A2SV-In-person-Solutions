class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        neighbor = lambda r, c: [
            (a, b) for a, b in [
                (r, c + 1),
                (r + 1, c),
                (r, c - 1),
                (r - 1, c)
            ] if 0 <= a < m and 0 <= b < n
        ]

        queue = deque([(sr, sc)])

        while queue:
            r, c = queue.popleft()
            old = image[r][c]
            image[r][c] = color

            for nr, nc in neighbor(r, c):
                if image[nr][nc] == old and image[nr][nc] != color:
                    queue.append((nr, nc))
        
        return image
        