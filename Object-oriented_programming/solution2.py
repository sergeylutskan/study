class BoundingRectangle():
    def __init__(self):
        self.x_points = []
        self.y_points = []
    def add_point(self, x, y):
        self.x_points.append(x)
        self.y_points.append(y)
    def left_x(self):
        return min(self.x_points)
    def right_x(self):
        return max(self.x_points)
    def bottom_y(self):
        return min(self.y_points)
    def top_y(self):
        return max(self.y_points)
    def width(self):
        return abs(max(self.x_points)-min(self.x_points))
    def height(self):
        return abs(max(self.y_points)-min(self.y_points))        


