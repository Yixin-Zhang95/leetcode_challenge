class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.neg_inf = float('-inf')
        self.current_max = self.neg_inf

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(x)
            self.current_max = x
        else:
            self.current_max = max(x, self.current_max)
            self.stack.append(x)

    def pop(self) -> int:
        ref = self.stack[-1]
        self.stack.pop()
        if ref == self.current_max:
            self.current_max = self.neg_inf
            for i in range(0, len(self.stack)):
                if self.stack[i] > self.current_max:
                    self.current_max = self.stack[i]
        return ref

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.current_max

    def popMax(self) -> int:
        ref = self.current_max

        #print('pre pop  {}'.format(self.stack))
        #print('pre pop len {}'.format(len(self.stack)))
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == self.current_max:
                #print('self.stck.pop',self.stack[i])
                self.stack.pop(i)
                #print('self.stck.pop', self.stack[-1])
                break

        #print('post pop len {}'.format(len(self.stack)))
        self.current_max = self.neg_inf
        for i in range(0, len(self.stack)):
            if self.stack[i] > self.current_max:
                self.current_max = self.stack[i]
                #print('self.stack[i]', self.stack[i])
                #print('self.current_max', self.current_max)
        return ref


obj = MaxStack()




inp1 = ["push","push","peekMax","push","top","popMax","top","push","push","push","top","push","pop","peekMax","popMax","push","popMax","push","top","top","popMax","popMax","push","push","push","peekMax","pop","push","peekMax","push","popMax","push","peekMax","pop","top","peekMax","top","peekMax","popMax","pop","top","push","peekMax","push","top","push","push","pop","push","push","push","popMax","top","push","popMax","peekMax","peekMax","push","pop","push","popMax","push","push","popMax","peekMax","pop","push","peekMax","popMax","popMax","popMax","push","push","peekMax","peekMax","pop","pop","popMax","push","peekMax","pop","top","top","push","push","top","push","pop","push","peekMax","popMax","push","peekMax","top","top","popMax","push","push","push","popMax"]
inp2 = [[-1919630],[7447491],[],[-2983652],[],[],[],[-3334898],[8846062],[2479120],[],[7050263],[],[],[],[-3743643],[],[-6196638],[],[],[],[],[-6436831],[-2835331],[3549770],[],[],[2643568],[],[-7853726],[],[-369996],[],[],[],[],[],[],[],[],[],[-9254475],[],[4462697],[],[7055993],[-4050360],[],[7162941],[-9620570],[6295114],[],[],[6366218],[],[],[],[-4009957],[],[4552628],[],[-7488568],[9893848],[],[],[],[1477827],[],[],[],[],[333068],[6486948],[],[],[],[],[],[-4255526],[],[],[],[],[-1598000],[-5135401],[],[-6279567],[],[-9375733],[],[],[-3078338],[],[],[],[],[8800414],[-4237017],[945773],[]]
expected = [None,None,7447491,None,-2983652,7447491,-2983652,None,None,None,2479120,None,7050263,8846062,8846062,None,2479120,None,-6196638,-6196638,-1919630,-2983652,None,None,None,3549770,3549770,None,2643568,None,2643568,None,-369996,-369996,-7853726,-2835331,-7853726,-2835331,-2835331,-7853726,-6436831,None,-3334898,None,4462697,None,None,-4050360,None,None,None,7162941,6295114,None,7055993,6366218,6366218,None,-4009957,None,6366218,None,None,9893848,6295114,-7488568,None,6295114,6295114,4552628,4462697,None,None,6486948,6486948,6486948,333068,1477827,None,-3334898,-4255526,-9620570,-9620570,None,None,-5135401,None,-6279567,None,-1598000,-1598000,None,-3078338,-3078338,-3078338,-3078338,None,None,None,8800414]
for i in range(0, len(inp1)):
    op = inp1[i]
    arg = inp2[i]
    if arg:
        res = getattr(obj, op)(arg[0])
    else:
        res = getattr(obj, op)()

    #print(res)
    #if res != expected[i]:
        #print('error: ', i, inp1[i], inp2[i])
        #print(res, expected[i])
        #break
