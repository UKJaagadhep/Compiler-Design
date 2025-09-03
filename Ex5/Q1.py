def build_symbol_table(expression):
    symbol_table = []
    for ch in expression:
        if ch.isalpha(): 
            symbol_table.append((ch, id(ch), "identifier"))
        elif ch in ['+', '-', '*', '=']:
            symbol_table.append((ch, id(ch), "operator"))
    return symbol_table

expr = input("Enter expression ending with $: ")
expr = expr.split('$')[0]

print("Given Expression:", expr)
print("\nSymbol Table display")
print("Symbol\tAddress\t\tType")

table = build_symbol_table(expr)
for sym, addr, typ in table:
    print(f"{sym}\t{addr}\t{typ}")

