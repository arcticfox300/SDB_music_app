from subprocess import check_output


def get_digits(n):
    digits = set()
    if n == 0:
        digits.add(0)
    while n > 0:
        digits.add(n % 10)
        n //= 10
    return digits


def problem12():
    n1 = int(input())
    n2 = int(input())
    digits_n1 = get_digits(n1)
    digits_n2 = get_digits(n2)
    if len(digits_n1 & digits_n2) == len(digits_n1):
        print("Numerele au proprietatea P")
    else:
        print("Numerele NU au proprietatea P")


def get_divizors(x, count, n):
    divizor = 2
    while x > 1:
        exponent = 0
        while x % divizor == 0:
            x //= divizor
            exponent += 1
        if exponent > 0:
            count += 1
        if count == n:
            return divizor, count
        divizor += 1
    return None, count

def the_n_element(n):
    if n == 1:
        return 1
    count = 1
    index = 1
    element = 1
    while count < n:
        element, count = get_divizors(index, count, n)
        index += 1
    return element

def problem13():
    n = int(input())
    print(the_n_element(n))

def is_perfect(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    if sum == number:
        return True
    return False

def find_perfect_number(number):
    index = number + 1
    while not is_perfect(index):
        index += 1
    return index


def problem15():
    number = int(input())
    print(find_perfect_number(number))


problem15()