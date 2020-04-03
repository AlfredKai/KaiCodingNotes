from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        group = {}
        groupCount = 0
        groupAggregate = {}
        mapping = {  # 0/1, 0\1
            '/': {
                '/': {
                    0: {
                        'top': 1,
                        'bottom': -1,
                        'left': 1,
                        'right': -1
                    },
                    1: {
                        'top': -1,
                        'bottom': 0,
                        'left': -1,
                        'right': 0
                    }
                },
                '\\': {
                    0: {
                        'top': 0,
                        'bottom': -1,
                        'left': 1,
                        'right': -1
                    },
                    1: {
                        'top': -1,
                        'bottom': 1,
                        'left': -1,
                        'right': 0
                    }
                },
                ' ': {
                    0: {
                        'top': 0,
                        'bottom': 0,
                        'left': 0,
                        'right': 0
                    },
                    1: {
                        'top': 0,
                        'bottom': 0,
                        'left': 0,
                        'right': 0
                    }
                }
            },
            '\\': {
                '/': {
                    0: {
                        'top': -1,
                        'bottom': 0,
                        'left': 1,
                        'right': -1
                    },
                    1: {
                        'top': 1,
                        'bottom': -1,
                        'left': -1,
                        'right': 0
                    }
                },
                '\\': {
                    0: {
                        'top': -1,
                        'bottom': 1,
                        'left': 1,
                        'right': -1
                    },
                    1: {
                        'top': 0,
                        'bottom': -1,
                        'left': -1,
                        'right': 0
                    }
                },
                ' ': {
                    0: {
                        'top': 0,
                        'bottom': 0,
                        'left': 0,
                        'right': 0
                    },
                    1: {
                        'top': 0,
                        'bottom': 0,
                        'left': 0,
                        'right': 0
                    }
                }
            },
            ' ': {
                '/': {
                    0: {
                        'top': -1,
                        'bottom': -1,
                        'left': -1,
                        'right': -1
                    },
                    1: {
                        'top': -1,
                        'bottom': -1,
                        'left': -1,
                        'right': -1
                    }
                },
                '\\': {
                    0: {
                        'top': -1,
                        'bottom': -1,
                        'left': -1,
                        'right': -1
                    },
                    1: {
                        'top': -1,
                        'bottom': -1,
                        'left': -1,
                        'right': -1
                    }
                },
                ' ': {
                    0: {
                        'top': -1,
                        'bottom': -1,
                        'left': -1,
                        'right': -1
                    },
                    1: {
                        'top': -1,
                        'bottom': -1,
                        'left': -1,
                        'right': -1
                    }
                }
            }
        }

        def decideGroup(groupA, groupB):
            nonlocal groupAggregate, groupCount
            group = -100
            if groupA != -1 and groupB != -1:
                if groupA < groupB:
                    groupAggregate[groupB] = groupA
                else:
                    groupAggregate[groupA] = groupB
                group = groupCount
                groupCount += 1
            elif groupA != -1:
                group = groupA
            else:
                group = groupB
            return group

        def checkNeighbor(r, c, dir):
            nonlocal grid, group
            # topIndex = leftIndex = bottomIndex = rightIndex = -1
            # topGroup = leftGroup = bottomGroup = rightGroup = -1
            if r-1 >= 0:  # top
                top = grid[r-1][c]
                topIndex = (r-1, c)
                topGroup = -1 if topIndex not in group else group[(r-1, c)]
            if c-1 >= 0:  # left
                left = grid[r][c-1]
                leftIndex = (r, c-1)
                leftGroup = -1 if leftIndex not in group else group[(r, c-1)]
            if r+1 < len(grid):  # bottom
                bottom = [r+1][c]
                bottomIndex = (r+1, c)
                bottomGroup = - \
                    1 if bottomIndex not in group else group[(r+1, c)]
            if c+1 < len(grid[r]):  # right
                right = grid[r][c+1]
                rightIndex = (r, c+1)
                rightGroup = -1 if rightIndex not in group else group[(r, c+1)]

            r = -1
            if grid[r][c] == '/':
                if dir == 'top':
                    if topGroup != -1:
                        r = topGroup[1] if top == '/' else topGroup[0]
                    return r
                elif dir == 'left':
                    if leftGroup != -1:
                        r = leftGroup[1] if left == '/' else leftGroup[0]
                    return r
                elif dir == 'bottom':
                    if bottomGroup != -1:
                        r = bottomGroup[0] if bottom == '/' else bottomGroup[1]
                    return r
                elif dir == 'right':
                    if rightGroup != -1:
                        r = rightGroup[0] if right == '/' else rightGroup[1]
                    return r

            if grid[r][c] == '\\':
                pass
            if grid[r][c] == ' ':
                pass

        # /
        for r in range(0, len(grid)):
            for c in range(0, len(grid[r])):
                top = left = bottom = right = ' '
                topGroup = leftGroup = bottomGroup = rightGroup = -1
                # check left
                if r-1 >= 0:  # top
                    mapping[grid[r][c]][grid[r-1][c]][0]['top']
                    top = grid[r-1][c]
                    if (r-1, c) in group:
                        # topGroup = group[(r-1, c)][1] if top == '/' else group[(r-1, c)][0]
                        topGroup = group[(r-1, c)][mapping[grid[r][c]][grid[r-1][c]][0]['top']]
                if c-1 >= 0:  # left
                    left = grid[r][c-1]
                    if (r, c-1) in group:
                        leftGroup = group[(r, c-1)][1] if left == '/' else group[(r, c-1)][0]

                if (r, c) not in group:
                    group[(r, c)] = [-1, -1]
                group[(r, c)][0] = decideGroup(topGroup, leftGroup)

                # check right
                if r+1 < len(grid):  # bottom
                    bottom = grid[r+1][c]
                    if (r+1, c) in group:
                        topGroup = group[(r-1, c)][1] if top == '/' else group[(r-1, c)][0]
                if c+1 < len(grid[r]):  # right
                    right = grid[r][c+1]

                print(' ', top)
                print(left, grid[r][c], right)
                print(' ', bottom)
        return group


# 123
# 456
# 789
a = Solution()
print(a.regionsBySlashes(['123', '456', '789']))
