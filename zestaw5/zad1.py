print("import rekucencja")
import rekurencja
print(rekurencja.factorial(6))
print(rekurencja.fibonacci(5))

print("from rekurencja import *")
from rekurencja import*
print(factorial(6))
print(fibonacci(5))

print("from rekurencja import fact, -||- as fib")
from rekurencja import factorial
from rekurencja import fibonacci as fib
print(factorial(6))
print(fib(5))

print("import rekurencja as rek")
import rekurencja as rek
print(rek.factorial(6))
print(rek.fibonacci(5))
