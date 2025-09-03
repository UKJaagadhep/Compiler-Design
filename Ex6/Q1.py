def Gen_IR(exp):
    e = list(exp.split("=")[1])
    op = ["/", "*", "+", "-"]
    stack = []
    variable_count = 1
    for i in op:
        for j in e[:]:
            if i == j:
                ind = e.index(j)
                stack.append(f"T{variable_count} := {e[ind-1]}{j}{e[ind+1]}")
                e.pop(ind-1)
                e.pop(ind-1)
                e.pop(ind-1)
                e.insert(ind-1, f"T{variable_count}")
                variable_count += 1
    stack.append(f"{exp[0]} := T{variable_count-1}")
                
    return stack
                
        
exp = input("Enter experssion : ")
result = Gen_IR(exp)
for i in result:    
    print(i)
    
