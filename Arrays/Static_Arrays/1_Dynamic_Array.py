class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity

if __name__ == "__main__":
    print("Creating DynamicArray with capacity 3")
    dyn_arr = DynamicArray(3)
    print(f"Initial size: {dyn_arr.getSize()}, capacity: {dyn_arr.getCapacity()}")
    print()
    
    print("Testing pushback:")
    for i in range(1, 6):
        dyn_arr.pushback(i * 10)
        print(f"Pushed {i * 10}: size = {dyn_arr.getSize()}, capacity = {dyn_arr.getCapacity()}")
    print()
    
    print("Testing get:")
    for i in range(dyn_arr.getSize()):
        print(f"Element at index {i}: {dyn_arr.get(i)}")
    print()
    
    print("Testing set:")
    dyn_arr.set(2, 999)
    print(f"Set index 2 to 999")
    print(f"Element at index 2 is now: {dyn_arr.get(2)}")
    print()
    
    print("Testing popback:")
    while dyn_arr.getSize() > 2:
        popped = dyn_arr.popback()
        print(f"Popped: {popped}, new size: {dyn_arr.getSize()}")
    print()
    
    print("Current array state:")
    print(f"Size: {dyn_arr.getSize()}, Capacity: {dyn_arr.getCapacity()}")
    print("Elements:", end=" ")
    for i in range(dyn_arr.getSize()):
        print(dyn_arr.get(i), end=" ")
    print("\n")
    
    print("Testing automatic resizing by adding many elements:")
    initial_capacity = dyn_arr.getCapacity()
    for i in range(10):
        dyn_arr.pushback(i * 100)
        if dyn_arr.getCapacity() != initial_capacity:
            print(f"  Capacity changed from {initial_capacity} to {dyn_arr.getCapacity()}")
            initial_capacity = dyn_arr.getCapacity()
    
    print(f"Final size: {dyn_arr.getSize()}, Final capacity: {dyn_arr.getCapacity()}")
    
    print("All elements:", end=" ")
    for i in range(dyn_arr.getSize()):
        print(dyn_arr.get(i), end=" ")
    print()