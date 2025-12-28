import math
	 
def solve_quadratic(a, b, c):
	delta = (b**2) - 4*a*c
	x1 = (-b + (math.sqrt(delta))) / (2*a)
	x2 = (-b - (math.sqrt(delta))) / (2*a)
	return x1, x2
	 
def main():
	print(solve_quadratic(0.083174, 3.343814, 5.032625))
	 
if __name__ == "__main__":
    main()