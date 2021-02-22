# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
num_complex = complex(input()) 
print(f"{abs(num_complex)}\n{cmath.phase(num_complex)}")
