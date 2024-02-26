from itertools import permutations


def evaluate(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return None


def find_expression(total):
    digits = "9876543210"
    operators = ["+", "-", ""]
    target = str(total)

    for perm in permutations(digits):
        for ops in permutations(operators, len(perm) - 1):
            exp = "".join(f"{perm[i]}{ops[i]}" for i in range(len(perm) - 1)) + perm[-1]
            if evaluate(exp) == int(target):
                return exp
    return None


target_number = 200
expression = find_expression(target_number)
if expression:
    print(f"Найдено выражение: {expression} = {target_number}")
else:
    print("Выражение не найдено.")
