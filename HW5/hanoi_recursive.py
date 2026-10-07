def hanoi_recursive(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi_recursive(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi_recursive(n - 1, auxiliary, target, source)
    
print("--- 1. Tower of Hanoi (n = 3) ---")
print("Recursive:")
hanoi_recursive(3, 'A', 'C', 'B')
