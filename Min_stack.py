class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)


    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()


    def top(self):
        return self.stack[-1]


    def getMin(self):
        return self.min_stack[-1]


obj = MinStack()
inp1 = ["push","push","push","getMin","pop","top","getMin"]
inp2 = [[-2],[0],[-3],[],[],[],[]]

for i in range(0, len(inp1)):
    op = inp1[i]
    arg = inp2[i]
    if arg:
        print(getattr(obj, op)(arg[0]))
    else:
        print(getattr(obj, op)())










