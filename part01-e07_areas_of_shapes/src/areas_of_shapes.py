#!/usr/bin/env python3

import math

def main():
    while True:
        shape = str(input("Choose a shape (triangle, rectangle, circle): "))
        if shape == "triangle":
            base = int(input("Give base of the triangle: "))
            height = int(input("Give height of the triangle: "))
            print(f"The area is {(base*height) / 2 :6f}")
        elif shape == "rectangle":
            width = int(input("Give width of the rectangle: "))
            height = int(input("Give height of the rectangle: "))
            print(f"The area is {width*height:6f}")
        elif shape == "circle":
            radius = int(input("Give radius of the circle: "))
            print(f"The area is {math.pi*(radius**2):6f}")    
        elif shape == "":
            break
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
