responces = [
    "Hello, My name is Ankit",
    "What may I Help you?",
    "Thank You",
    "Bye-Bye",
    "Sorry, I don't Know this",
    "But Next time surely I will do for you"
]

# ------------------- Math Functions -------------------
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def fibonacci(n):
    seq = []
    a, b = 0, 1
    for i in range(n):
        seq.append(a)
        a, b = b, a+b
    return seq

def is_prime(n):
    if n <= 1:
        return f"{n} is not a prime number"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f"{n} is not a prime number"
    return f"{n} is a prime number"

def addition(*args):
    return sum(args)

def subtraction(*args):
    if len(args) == 0:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def division(*args):
    if len(args) == 0:
        return "No numbers given"
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Division by zero not allowed"
        result /= num
    return result

# ------------------- System Functions -------------------
def end():
    print(responces[2])
    print(responces[3])

def extract_num(text):
    l1 = []
    for w in text.replace(",", " ").split():  # ✅ also split by commas
        try:
            l1.append(int(w))
        except:
            pass
    return l1

def ankit():
    print("Ankit kumar gupta is student of Inmantec , He is in 3rd year of BCA")


# ------------------- Command Dictionary -------------------
operations = {
    "FACTORIAL": factorial,
    "FACT": factorial,
    "FIBONACCI": fibonacci,
    "FIB": fibonacci,
    "PRIME": is_prime,
    "ADD": addition,
    "SUM": addition,
    "ADDITION": addition,
    "PLUS": addition,
    "SUB": subtraction,
    "SUBTRACTION": subtraction,
    "DIFFERENCE": subtraction,
    "MUL": multiply,
    "MULTIPLY": multiply,
    "DIV": division,
    "DIVIDE": division,
    "DIVISION": division
}

commands = {
    "ANKIT": ankit,
    "BYE": end,
    "BYE-BYE": end,
    "EXIT": end,
}
