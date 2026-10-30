class MinStack:

    def __init__(self):
        #Initialize an array
        self.stack_list = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack_list.append(val)

        # If min stack is empty, insert or if top element of min stack is > than val, insert val as top element
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        
        return
        

    def pop(self) -> None:
        # If value popped is current minimum, pop it from min_stack too
        if self.min_stack[-1] == self.stack_list[-1]:
            self.min_stack.pop()
        
        self.stack_list.pop()

        return
        

    def top(self) -> int:
        # Return the first element 
        return self.stack_list[-1]
        

    def getMin(self) -> int:
        # Return the top element of the min stack
        return self.min_stack[-1]
        
