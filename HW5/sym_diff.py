def sym_diff(expr, var="x"):
    # Constant rule: d/dx(c) = 0
    if isinstance(expr, (int, float)):
        return 0
    
    # Variable rule: d/dx(x) = 1, d/dx(y) = 0
    if isinstance(expr, str):
        return 1 if expr == var else 0
    
    # Composite expressions: (op, left, right)
    op, u, v = expr[0], expr[1], expr[2]
    
    if op == "+":
        # (u + v)' = u' + v'
        return ("+", sym_diff(u, var), sym_diff(v, var))
    
    elif op == "-":
        # (u - v)' = u' - v'
        return ("-", sym_diff(u, var), sym_diff(v, var))
    
    elif op == "*":
        # (u * v)' = u' * v + u * v'
        return ("+", ("*", sym_diff(u, var), v), ("*", u, sym_diff(v, var)))
    
    elif op == "^":
        # Power rule d/dx(x^n) where n is a constant
        if u == var and isinstance(v, (int, float)):
            return ("*", v, ("^", u, v - 1))
        else:
            raise NotImplementedError("General chain rule for functions not implemented.")
            
    raise ValueError(f"Unknown operation: {op}")

print("\n--- 2. Symbolic Differentiation ---")
    # Expression: x^3 + 2*x
expr = ("+", ("^", "x", 3), ("*", 2, "x"))
print("Original expression:", expr)
print("Derivative d/dx:", sym_diff(expr, "x"))