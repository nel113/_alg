def hanoi_iterative(n, source, target, auxiliary):
    # Stack stores tuples of: (n, source, target, auxiliary)
    stack = [(n, source, target, auxiliary)]
    
    while stack:
        n, src, tgt, aux = stack.pop()
        
        if n == 1:
            print(f"Move disk 1 from {src} to {tgt}")
        else:
            # Push in reverse order of execution (LIFO)
            # Step 3: Move n-1 disks from aux to tgt
            stack.append((n - 1, aux, tgt, src))
            # Step 2: Move disk n from src to tgt
            stack.append((1, src, tgt, aux))
            # Step 1: Move n-1 disks from src to aux
            stack.append((n - 1, src, tgt, aux))    
            
print("\nIterative:")
hanoi_iterative(3, 'A', 'C', 'B')