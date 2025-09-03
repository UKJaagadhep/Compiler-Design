def optimize_code(code):
    optimized = []
    used_vars = set()

    for stmt in code:
        left, right = stmt.split("=")
        left, right = left.strip(), right.strip()
        for ch in right:
            if ch.isalpha():
                used_vars.add(ch)

    for stmt in code:
        left, right = stmt.split("=")
        left, right = left.strip(), right.strip()
        if left in used_vars or stmt == code[-1]:
            if stmt not in optimized: 
                optimized.append(stmt)

    return optimized

code = ["a = S", "b = a + c", "c = c * 5"]

print("Intermediate Code:")
for c in code:
    print(c)

print("\nOptimized Code:")
for c in optimize_code(code):
    print(c)

