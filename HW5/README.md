

## 1. Tower of Hanoi (`hanoi.py`)

### Overview

Solves the classic Tower of Hanoi puzzle using both recursive and non-recursive (stack-based iterative) strategies.

### API Reference

* **`hanoi_recursive(n, source, target, auxiliary)`**
* **Description:** Solves the puzzle by breaking it down into subproblems using function recursion.
* **Time Complexity:** $O(2^n)$
* **Space Complexity:** $O(n)$ call stack depth.


* **`hanoi_iterative(n, source, target, auxiliary)`**
* **Description:** Simulates the recursive call stack using an explicit stack list (`LIFO`) without recursive function calls.
* **Time Complexity:** $O(2^n)$
* **Space Complexity:** $O(n)$ explicit stack storage.



---

## 2. Symbolic Differentiation (`sym_diff.py`)

### Overview

Recursively computes the symbolic derivative $\frac{d}{dx}$ of a mathematical expression represented as nested tuples.

### Expression Grammar

| Syntax | Math Equivalent | Example Tuple Representation |
| --- | --- | --- |
| `int` / `float` | $c$ | `5` |
| `str` | $x$ | `"x"` |
| `("+", u, v)` | $u + v$ | `("+", "x", 3)` |
| `("-", u, v)` | $u - v$ | `("-", "x", 2)` |
| `("*", u, v)` | $u \cdot v$ | `("*", 2, "x")` |
| `("^", u, n)` | $u^n$ | `("^", "x", 3)` |

### API Reference

* **`sym_diff(expr, var="x")`**
* **Parameters:**
* `expr` *(tuple | str | int | float)*: Expression tree structure.
* `var` *(str)*: Variable to differentiate with respect to (default: `"x"`).


* **Returns:** Nested tuple containing the differentiated expression structure.



---

## 3. Functional Utilities & Loopless Bubble Sort (`functional_sort.py`)

### Overview

Reimplements standard functional paradigms using pure tail/head recursion without Python loop constructs (`for`, `while`), then constructs a loopless Bubble Sort using pure recursion.

### API Reference

#### Custom Functional Higher-Order Functions

* **`my_map(func, lst)`**
* **Description:** Recursively applies `func` to every element in `lst`.


* **`my_filter(func, lst)`**
* **Description:** Recursively filters elements from `lst` where `func(elem)` evaluates to `True`.


* **`my_reduce(func, lst, initial=None)`**
* **Description:** Recursively accumulates values across `lst` applying `func(accumulator, current)`.



#### Loopless Bubble Sort

* **`bubble_pass(lst)`**
* **Description:** Performs a single recursive pass through `lst`, swapping adjacent out-of-order pairs and pushing the largest element to the tail.


* **`bubble_sort_recursive(lst)`**
* **Description:** Recursively triggers `bubble_pass` on shrinking list slices until fully sorted.
* **Time Complexity:** $O(n^2)$ worst/average case.
* **Space Complexity:** $O(n^2)$ total frames created during recursive list allocation.