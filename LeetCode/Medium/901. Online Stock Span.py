from collections import namedtuple

class StockSpanner:

    def __init__(self):
        self.monoStack = []
        self.count = 0

    def next(self, price: int) -> int:
        r = 0
        for i in reversed(range(len(self.monoStack))):
            if self.monoStack[i][0] > price:
                r = self.count - self.monoStack[i][1]
                break
        else:
            r = self.count + 1
        while self.monoStack and self.monoStack[-1][0] <= price:
            self.monoStack.pop()
        self.monoStack.append((price, self.count))
        self.count += 1
        return r

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next(100)
param_1 = obj.next(80)
param_1 = obj.next(60)
param_1 = obj.next(70)
param_1 = obj.next(60)
param_1 = obj.next(75)
param_1 = obj.next(85)