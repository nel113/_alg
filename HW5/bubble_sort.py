# Custom recursive map
def my_map(func, lst):
    if not lst:
        return []
    return [func(lst[0])] + my_map(func, lst[1:])

# Custom recursive filter
def my_filter(func, lst):
    if not lst:
        return []
    if func(lst[0]):
        return [lst[0]] + my_filter(func, lst[1:])
    return my_filter(func, lst[1:])

# Custom recursive reduce
def my_reduce(func, lst, initial=None):
    if initial is None:
        if not lst:
            raise TypeError("reduce() of empty sequence with no initial value")
        return my_reduce(func, lst[1:], lst[0])
    if not lst:
        return initial
    return my_reduce(func, lst[1:], func(initial, lst[0]))

# --- Loopless Bubble Sort ---

# Single pass over array using recursion
def bubble_pass(lst):
    if len(lst) <= 1:
        return lst
    if lst[0] > lst[1]:
        # Swap adjacent elements and continue pass
        res = bubble_pass([lst[0]] + lst[2:])
        return [lst[1]] + res
    else:
        res = bubble_pass([lst[1]] + lst[2:])
        return [lst[0]] + res

# Repeat passes recursively until array length is reduced to 1
def bubble_sort_recursive(lst):
    if len(lst) <= 1:
        return lst
    # Perform one pass to float the largest element to the end
    passed = bubble_pass(lst)
    # Recursively sort the remaining elements and append the last element
    return bubble_sort_recursive(passed[:-1]) + [passed[-1]]

print("\n--- 3. Custom Functions & Loopless Bubble Sort ---")
nums = [5, 2, 9, 1, 7, 3]
    
print("Custom Map (x * 2):", my_map(lambda x: x * 2, nums))
print("Custom Filter (even only):", my_filter(lambda x: x % 2 == 0, nums))
print("Custom Reduce (sum):", my_reduce(lambda a, b: a + b, nums))
    
print("Original list:", nums)
print("Sorted list (Loopless Bubble Sort):", bubble_sort_recursive(nums))