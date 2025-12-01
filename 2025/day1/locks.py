class Lock:
    def __init__(self, pos, size=100):
        self.idx = pos
        self.current_position = pos
        self.values = list(range(0, 100))
        self.clicks = 0

    def shift_left(self, rotate_by):
        for _ in range(rotate_by): # Example: Access 10 elements
            self.idx = (self.idx - 1) % len(self.values)
            if self.idx == 0:
                self.clicks += 1

    def shift_right(self, rotate_by):
        for _ in range(rotate_by): # Example: Access 10 elements
            self.idx = (self.idx + 1) % len(self.values)
            if self.idx == 0:
                self.clicks += 1

    def get_position(self):
        return self.idx
    
    def get_clicks(self):
        return self.clicks
  
   
def main():
    lock = Lock(50, 100)
    counter = 0
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(f"direction: {line[0]}, rotate_by: {line[1:]}")
            # check first character for direction
            direction, rotate_by = line[0], line[1:]
            rotate_by = int(rotate_by)
            if direction.upper() == "L":
                lock.shift_left(rotate_by)
            elif direction.upper() == "R":
                lock.shift_right(rotate_by)

            print(f"Current Position: {lock.get_position()}")
            counter += 1 if lock.get_position() == 0 else 0
            
    print(f"Counter is {counter}, clicks is {lock.get_clicks()}")

def test():
    lock = Lock(50, 100)
    assert lock.get_position() == 50
    lock.shift_left(190)
    print(f"New position: {lock.get_position()}")
    assert lock.get_position() == 60
    lock.shift_right(20)
    print(f"New position: {lock.get_position()}")    
    assert lock.get_position() == 80
    lock.shift_right(195)
    print(f"New position: {lock.get_position()}")    
    assert lock.get_position() == 75
    lock.shift_left(10)
    print(f"New position: {lock.get_position()}")    
    assert lock.get_position() == 65
    print("All tests passed.")

if __name__ == "__main__":
    main()
    #test()