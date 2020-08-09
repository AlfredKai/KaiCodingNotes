from typing import List

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # ["David","3","Ceviche"]
        foods = set()
        tableNum = set()
        tableDish = {}
        for order in orders:
            tableN = int(order[1])
            if (tableN, order[2]) not in tableDish:
                tableDish[(tableN, order[2])] = 1
            else:
                tableDish[(tableN, order[2])] += 1
            if order[2] not in foods:
                foods.add(order[2])
            if tableN not in tableNum:
                tableNum.add(tableN)
        heads = ['Table']
        foods = sorted(foods)
        for f in foods:
            heads.append(f)
        result = [heads]
        for t in sorted(tableNum):
            row = []
            row.append(str(t))
            for f in foods:
                if (t,f) in tableDish:
                    row.append(str(tableDish[(t, f)]))
                else:
                    row.append('0')
            result.append(row)
        return result


# study python sorted()

a = Solution()
a.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]])