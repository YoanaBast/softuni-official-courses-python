# Create a function that calculates and returns the area of a rectangle by a given width and height. Print the result on the console.

rectangle_area = lambda w, h: w * h
width = int(input())
height = int(input())
print(rectangle_area(width, height))