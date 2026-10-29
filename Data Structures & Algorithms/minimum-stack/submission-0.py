class MinStack:

    def __init__(self):
        self.stack_list = []

    def push(self, val: int) -> None:
        self.stack_list.append(val)
        return
        

    def pop(self) -> None:
        self.stack_list.pop()
        return

    def top(self) -> int:
        return self.stack_list[-1]
        

    def getMin(self) -> int:
        set_list = sorted(set(self.stack_list))
        return set_list[0]
