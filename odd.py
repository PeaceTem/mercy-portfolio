def calculate_powers(a, b, n, m):
    if n + m != 10:
        return "The sum of n and m must be 10."
    print(f"{a}^{n} * {b}^{m} = {(a ** n) * (b ** m)}")

# # Example usage:
# a = 2
# b = 3
# n = 6
# m = 4
# result = calculate_powers(a, b, n, m)
# print(result)

def check():
    for j in range(1, 11):
        a = 1 - j / 10
        b = a + (j)

        for n in range(0, 11):
            m = 10 - n
            calculate_powers(a, b, n, m)
        print()

check()

for n in range(0, 11):
    m = 10 - n
    calculate_powers(0.5, 4.1, n, m)
    calculate_powers(0.8, 4.1, n, m)
    calculate_powers(0.5, 2, n, m)
    print()

print()
