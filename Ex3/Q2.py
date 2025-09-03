def leftfactoring(grammar_list):
    result = []
    for rule in grammar_list:
        lhs, rhs = rule.split(" -> ")
        rhs_parts = rhs.split(" | ")

        prefix = None
        for i in range(1, min(len(p) for p in rhs_parts)+1):
            first = rhs_parts[0][:i]
            if all(p.startswith(first) for p in rhs_parts):
                prefix = first
            else:
                break

        if prefix and len(rhs_parts) > 1:
            new_lhs = lhs + "'"
            beta = [p[len(prefix):] or "ε" for p in rhs_parts]
            result.append(f"{lhs} -> {prefix}{new_lhs}")
            result.append(f"{new_lhs} -> " + " | ".join(beta))
        else:
            result.append(rule)

    return result

n = int(input("Enter number of Grammar rules: "))
grammars = []
for i in range(n):
    grammars.append(input(f"Enter Grammar {i+1}: "))
output = leftfactoring(grammars)
for g in output:
    print(g)
