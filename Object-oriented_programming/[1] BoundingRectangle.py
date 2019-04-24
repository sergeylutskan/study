# Processes some points and builds a minimum-sized rectangle around them, which includes all these points. 
# If a point lies on the border of a rectangle, it is considered to be a part of it.

from solution2 import BoundingRectangle

rect = BoundingRectangle()
rect.add_point(-11, -12)
rect.add_point(13, -14)
rect.add_point(-15, 10)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print()
rect.add_point(-21, -12)
rect.add_point(13, -14)
rect.add_point(-15, 36)
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print()
rect.add_point(-21, 78)
rect.add_point(13, -14)
rect.add_point(-55, 36)
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
print()
