# Python code to demonstrate naive method
# to compute factorial
n = input("Введи число, факториал которого следует вычислить: ")
n = int(n)
zeros = str(n)
print(len(zeros) - 1)
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(f"The factorial of {n} is : ", end="")
print(fact)