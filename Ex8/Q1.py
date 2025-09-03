def generate_target_code(intermediate_code):
    target_code = []
    reg_count = 1 

    for stmt in intermediate_code:
        left, right = stmt.split("=")
        left = left.strip()
        right = right.strip()

        if any(op in right for op in ["+", "-", "*", "/"]):
            tokens = right.split()
            op1, operator, op2 = tokens[0], tokens[1], tokens[2]
            target_code.append(f"LOAD R{reg_count}, {op1}")
            target_code.append(f"{operator_map(operator)} R{reg_count}, {op2}")
            target_code.append(f"STORE {left}, R{reg_count}")
        else:
            target_code.append(f"LOAD R{reg_count}, {right}")
            target_code.append(f"STORE {left}, R{reg_count}")

    return target_code

def operator_map(op):
    return {
        "+": "ADD",
        "-": "SUB",
        "*": "MUL",
        "/": "DIV"
    }[op]

intermediate = [
    "t1 = b + c",
    "t2 = t1 * d",
    "a = t2"
]

result = generate_target_code(intermediate)

print("Target Code:")
for line in result:
    print(line)
