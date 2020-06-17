from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set()
        startColor = image[sr][sc]
        stack = [(sr,sc)]
        while stack:
            node = stack.pop()
            visited.add(node)
            r = node[0]
            c = node[1]
            image[r][c] = newColor
            if r-1 >= 0 and image[r-1][c] == startColor and (r-1,c) not in visited:
                stack.append((r-1, c))
            if c-1 >= 0 and image[r][c-1] == startColor and (r,c-1) not in visited:
                stack.append((r, c-1))
            if r+1 < len(image) and image[r+1][c] == startColor and (r+1,c) not in visited:
                stack.append((r+1, c))
            if c+1 < len(image[0]) and image[r][c+1] == startColor and (r,c+1) not in visited:
                stack.append((r, c+1))
        return image

