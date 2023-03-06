import random

class Blob:

    def __init__(self, color, x_bound, y_bound,size_range=(4,8),move_range=(-1,2)):
        self.color = color
        self.x_bound = x_bound
        self.y_bound = y_bound
        self.size = random.randrange(size_range[0], size_range[1])
        self.move_range = move_range
        self.x = random.randrange(0, self.x_bound)
        self.y = random.randrange(0, self.y_bound)


    def check_bounds_before_move(self, enforcement=True):
        move_x = random.randrange(self.move_range[0],self.move_range[1])
        move_y = random.randrange(self.move_range[0],self.move_range[1])
        new_x = (self.x + move_x)
        new_y = (self.y + move_y)

        if enforcement:
            if new_x < 0:
                new_x = 0
            elif new_x > self.x_bound:
                new_x = self.x_bound

            if new_y < 0:
                new_y = 0
            elif new_y > self.y_bound:
                new_y = self.y_bound
            
            return [new_x, new_y]

        else: return [new_x, new_y]
            
    def move(self, list=[]):
        if list == []:
            self.x = random.randrange(self.move_range[0],self.move_range[1])
            self.y = random.randrange(self.move_range[0],self.move_range[1])
        else:
            self.x = list[0]
            self.y = list[1]
        
        return self
            
