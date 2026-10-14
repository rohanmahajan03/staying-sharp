# [3,4,5,6,2]
# we must only add to min_stack if val > min_stack[-1]
#[3,]


# [3,3]
# [3,]
class MinStack:

    def __init__(self):
        self.curr_stack = []
        self.min_stack = []

        

    def push(self, val: int) -> None:
        self.curr_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        val = self.curr_stack.pop()
        if val == self.min_stack[-1]:
           self. min_stack.pop()
        

    def top(self) -> int:
        return self.curr_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
