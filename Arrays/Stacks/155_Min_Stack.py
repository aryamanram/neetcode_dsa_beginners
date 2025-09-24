class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

if __name__ == "__main__":
    minStack = MinStack()
    
    print("MinStack Operations Test")
    print("-" * 30)
    
    print("Test 1: Basic operations")
    minStack.push(-2)
    print(f"Push -2")
    print(f"  Current min: {minStack.getMin()}")
    
    minStack.push(0)
    print(f"Push 0")
    print(f"  Current min: {minStack.getMin()}")
    
    minStack.push(-3)
    print(f"Push -3")
    print(f"  Current min: {minStack.getMin()}")
    print(f"  Top element: {minStack.top()}")
    
    minStack.pop()
    print(f"Pop")
    print(f"  Current min: {minStack.getMin()}")
    print(f"  Top element: {minStack.top()}")
    print()
    
    print("Test 2: New MinStack with increasing then decreasing values")
    minStack2 = MinStack()
    
    operations = [
        ("push", 5),
        ("push", 3),
        ("push", 7),
        ("push", 1),
        ("push", 9),
    ]
    
    for op, val in operations:
        if op == "push":
            minStack2.push(val)
            print(f"Push {val}")
            print(f"  Stack top: {minStack2.top()}, Min: {minStack2.getMin()}")
    
    print("\nPopping elements:")
    while True:
        try:
            current_top = minStack2.top()
            current_min = minStack2.getMin()
            print(f"Before pop - Top: {current_top}, Min: {current_min}")
            minStack2.pop()
            if len(minStack2.stack) > 0:
                print(f"After pop  - Top: {minStack2.top()}, Min: {minStack2.getMin()}")
            else:
                print("Stack is now empty")
                break
        except:
            break
    print()
    
    print("Test 3: Duplicate minimum values")
    minStack3 = MinStack()
    
    values = [2, 2, 1, 3, 1, 4]
    for val in values:
        minStack3.push(val)
        print(f"Push {val} -> Min: {minStack3.getMin()}")
    
    print("\nPopping with duplicate minimums:")
    for _ in range(3):
        print(f"Pop -> Top: {minStack3.top()}, Min: {minStack3.getMin()}")
        minStack3.pop()
    print()
    
    print("Test 4: All same values")
    minStack4 = MinStack()
    
    for _ in range(3):
        minStack4.push(5)
    print(f"Pushed 5 three times")
    print(f"Min: {minStack4.getMin()}, Top: {minStack4.top()}")
    
    minStack4.pop()
    print(f"After one pop - Min: {minStack4.getMin()}, Top: {minStack4.top()}")