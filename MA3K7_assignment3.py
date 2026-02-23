import random
def numbergame(n):
    numbers = list(range(1, n + 1))
    while len(numbers)  > 1:
        chosen = random.sample(numbers, 2)
        for num in chosen:
            numbers.remove(num)
        numbers.append(abs(chosen[0] - chosen[1]))
    return numbers[0]

upto = 100

for n in range(1,upto+1):
    q = numbergame(n)
    print("n =", n, "// ended on", q, "// parity =", "even" if q % 2 == 0 else "odd")

#odd odd even even repeat
#hypothesis: if n is 1 or 2 more than a multiple of 4, it is odd. if n is 1 or 2 less than a multiple of 4, it is even. Why??
    