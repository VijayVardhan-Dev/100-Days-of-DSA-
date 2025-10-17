# 🔹 1. What is an Array?

An **array** is a **collection of elements** of the **same data type**, stored in **contiguous memory locations**.

Think of it as a **row of boxes** — each box holds one element, and every box can be accessed using its **index (position)**.

### Example:

```python
arr = [10, 20, 30, 40, 50]

```

| Index | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| Value | 10 | 20 | 30 | 40 | 50 |

---

## 🔹 2. Types of Arrays

1. **One-Dimensional Array (1D):**
    - A simple list of elements.
    - Example: `[10, 20, 30]`
2. **Two-Dimensional Array (2D):**
    - An array of arrays (like a matrix or table).
    - Example:
        
        ```python
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        
        ```
        
3. **Multi-Dimensional Arrays (3D, 4D, …):**
    - Arrays within arrays (used in simulations, 3D graphics, etc.)
4. **Dynamic Arrays (Python lists):**
    - Can change size at runtime.
    - Example: You can append or remove elements easily.

---

## 🔹 3. Array in Memory

- Stored **contiguously** in memory (elements one after another).
- Accessed by calculating **base address + index × size of element**.

Example:

If base address = 1000, element size = 4 bytes,

then `arr[3]` is at `1000 + 3×4 = 1012`.

This is why arrays have **O(1)** access time — direct computation!

---

## 🔹 4. Creating an Array

### Using List (Dynamic Array)

```python
arr = [1, 2, 3, 4, 5]

```

### Using `array` module (Fixed type)

```python
import array
arr = array.array('i', [10, 20, 30])

```

- `'i'` → integer type code
- You can also use `'f'` for float, `'d'` for double, etc.

---

## 🔹 5. Insertion Operation

Adding a new element to the array.

### Example:

```python
arr = [10, 20, 30, 40]
arr.insert(2, 25)   # insert 25 at index 2
print(arr)  # [10, 20, 25, 30, 40]

```

### Time Complexity:

- **Best Case:** O(1) (at the end)
- **Worst Case:** O(n) (at the beginning or middle)

---

## 🔹 6. Traversal Operation

Visiting every element in the array once.

```python
arr = [10, 20, 30, 40, 50]
for element in arr:
    print(element)

```

### Time Complexity:

- **O(n)** — each element is accessed once.

---

## 🔹 7. Accessing Elements

Access using index → **O(1)** time.

```python
arr = [10, 20, 30, 40, 50]
print(arr[2])  # Output: 30

```

### Note:

Accessing out of range index → `IndexError`

---

## 🔹 8. Searching in Array

### (a) **Linear Search** — O(n)

Check each element until found.

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
print(linear_search(arr, 30))  # Output: 2

```

### (b) **Binary Search** — O(log n)

Works **only on sorted arrays**.

```python
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

```

---

## 🔹 9. Deletion Operation

Removing an element.

```python
arr = [10, 20, 30, 40]
arr.remove(30)
print(arr)  # [10, 20, 40]

```

### Time Complexity:

- **Best Case:** O(1) (last element)
- **Worst Case:** O(n) (first or middle element)

---

## 🔹 10. Time and Space Complexity Summary

| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access | O(1) | O(n) |
| Insertion | O(n) | O(n) |
| Deletion | O(n) | O(n) |
| Traversal | O(n) | O(n) |
| Search (Linear) | O(n) | O(1) |
| Search (Binary) | O(log n) | O(1) |

---

## 🔹 11. Practice Ideas

✅ Write your own functions for:

- Insert at beginning, end, middle
- Delete by index or by value
- Linear & binary search
- Reverse an array
- Find min/max
- Find sum and average

✅ Solve problems:

- Move all zeros to end
- Find missing number
- Merge two sorted arrays
- Rotate array by k positions

---

# 🧮 Two-Dimensional Arrays (2D Arrays)

---

## 🔹 12. What is a 2D Array?

A **2D array** is like a **table (matrix)** — it has rows and columns.

Example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

```

| Row | Col0 | Col1 | Col2 |
| --- | --- | --- | --- |
| 0 | 1 | 2 | 3 |
| 1 | 4 | 5 | 6 |
| 2 | 7 | 8 | 9 |

---

## 🔹 13. Creation

```python
rows, cols = 3, 3
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

```

---

## 🔹 14. Insertion

```python
matrix[0][1] = 10
print(matrix)

```

---

## 🔹 15. Accessing Elements

```python
print(matrix[1][2])  # Access element at row 1, col 2

```

---

## 🔹 16. Traversal

```python
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()

```

---

## 🔹 17. Searching

```python
def search(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return (i, j)
    return -1

```

---

## 🔹 18. Deletion

You can remove an element or an entire row.

```python
matrix[1].remove(5)     # Remove element 5 from row 1
del matrix[2]           # Delete entire row

```

---

## 🔹 19. Time and Space Complexity (2D)

| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access | O(1) | O(m×n) |
| Traversal | O(m×n) | O(m×n) |
| Search | O(m×n) | O(1) |
| Insertion | O(m×n) | O(m×n) |
| Deletion | O(m×n) | O(m×n) |

---

## 🔹 When to Use Arrays

✅ Use **arrays** when:

- You know the number of elements in advance.
- You want **fast access** using indices.
- You want **contiguous memory** for performance.
- You are implementing **mathematical operations, matrices, or data tables.**

✅ Avoid arrays when:

- You need frequent insertions/deletions → use **Linked List** instead.
- You need key-based access → use **Dictionary**.
- You don’t know size beforehand and need flexibility → use **List** (Python)
