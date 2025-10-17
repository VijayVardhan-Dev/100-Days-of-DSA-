# 🧠 **Time Complexity — Complete Notes (Python Edition)**

---

## 📘 **1. What Is Time Complexity?**

**Time Complexity** measures how the running time of an algorithm changes as the input size `n` increases.

It’s not measured in seconds, but in **growth rate** — how fast the algorithm “slows down” when the input grows.

> 💡 Think of it as: “How well does my algorithm scale when the data grows larger?”
> 

---

## ⚙️ **2. Why Use Time Complexity Instead of Actual Time?**

Actual time depends on:

- CPU speed
- Programming language
- Compiler/interpreter
- Machine load

✅ **Time Complexity** abstracts all of that. It compares **algorithms logically**, not physically.

---

## 🧩 **3. Big-O Notation (Upper Bound)**

**Big-O** tells us how fast the running time increases as input size increases — it’s the **worst-case** growth rate.

| Notation | Name | Description |
| --- | --- | --- |
| O(1) | Constant | Same time regardless of input size |
| O(log n) | Logarithmic | Reduces the problem by a constant factor each time |
| O(n) | Linear | Time grows directly with input size |
| O(n log n) | Linearithmic | Grows slightly faster than linear (sorting) |
| O(n²) | Quadratic | Two nested loops |
| O(n³) | Cubic | Three nested loops |
| O(2ⁿ) | Exponential | Recursive branching (Fibonacci) |
| O(n!) | Factorial | All possible permutations |

---

## 🧮 **4. Steps to Analyze Time Complexity**

### 🔹 Step 1: Identify Input Size `n`

- For a list → `n = len(list)`
- For a matrix → `n = number of rows/columns`
- For a string → `n = len(string)`

---

### 🔹 Step 2: Count the Repeating Operations

Focus on what repeats — loops, recursion, or repeated function calls.

---

### 🔹 Step 3: Ignore Constants & Lower Terms

If time = `3n² + 5n + 2`

→ **O(n²)** (since for large `n`, `n²` dominates)

---

### 🔹 Step 4: Keep Only the Highest Growing Term

Big-O keeps only the dominant term, representing how runtime **scales**.

---

## 📚 **5. Common Examples in Python**

---

### ✅ Example 1: Constant Time → O(1)

```python
a = 5
b = 10
c = a + b

```

**Explanation:**

No loops, no recursion — executes in constant time.

---

### ✅ Example 2: Linear Time → O(n)

```python
def print_numbers(n):
    for i in range(n):
        print(i)

```

**Explanation:**

Loop runs `n` times → linear relationship.

---

### ✅ Example 3: Quadratic Time → O(n²)

```python
def print_pairs(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

```

**Explanation:**

Outer loop → `n` times

Inner loop → `n` times

Total = `n * n = n²`

---

### ✅ Example 4: Logarithmic Time → O(log n)

```python
def log_example(n):
    i = 1
    while i < n:
        i *= 2

```

**Explanation:**

`i` doubles every iteration → number of iterations = log₂(n)

---

### ✅ Example 5: Linearithmic Time → O(n log n)

```python
def linear_log(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 2

```

**Explanation:**

Outer loop → `n`

Inner loop → `log n`

Total = `n * log n`

---

### ✅ Example 6: Exponential → O(2ⁿ)

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

```

**Explanation:**

Each call spawns two recursive calls → exponential growth.

---

### ✅ Example 7: Factorial → O(n!)

```python
def permute(s, l=0):
    if l == len(s) - 1:
        print(''.join(s))
    else:
        for i in range(l, len(s)):
            s[l], s[i] = s[i], s[l]
            permute(s, l + 1)
            s[l], s[i] = s[i], s[l]

```

**Explanation:**

Generates all possible permutations — factorial time.

---

## ⚡ **6. Common Patterns to Recognize Instantly**

| Pattern | Time Complexity | Example |
| --- | --- | --- |
| Single loop | O(n) | Traverse list |
| Two nested loops | O(n²) | Double loop |
| Logarithmic loop | O(log n) | While `i *= 2` |
| Loop + inner log loop | O(n log n) | Sorts |
| Two separate loops (not nested) | O(n + n) → O(n) | Two passes |
| Recursive divide & conquer | O(n log n) | Merge sort |
| Triple nested loop | O(n³) | 3D traversal |

---

## 🧠 **7. Space Complexity (Quick Intro)**

**Space Complexity** = extra memory your program uses besides input.

| Example | Space |
| --- | --- |
| Basic variables | O(1) |
| Array/list of n items | O(n) |
| 2D array | O(n²) |
| Recursive depth | O(depth) |

---

## 🧩 **8. Shortcut Rules**

| Python Code Pattern | Time Complexity |
| --- | --- |
| `for i in range(n):` | O(n) |
| `for i in range(n): for j in range(n):` | O(n²) |
| `for i in range(n): for j in range(i):` | O(n²/2) → O(n²) |
| `while i < n: i *= 2` | O(log n) |
| `for i in range(n): while j < n: j *= 2` | O(n log n) |
| Three nested loops | O(n³) |
| Recurrence `T(n)=T(n/2)+O(1)` | O(log n) |
| Recurrence `T(n)=2T(n/2)+O(1)` | O(n) |
| Recurrence `T(n)=2T(n/2)+O(n)` | O(n log n) |

---

## 🔍 **9. Real-World Intuition**

| Algorithm | Time Complexity | Type |
| --- | --- | --- |
| Linear Search | O(n) | Linear |
| Binary Search | O(log n) | Logarithmic |
| Bubble Sort | O(n²) | Quadratic |
| Insertion Sort | O(n²) | Quadratic |
| Merge Sort | O(n log n) | Efficient |
| Quick Sort | O(n log n) average, O(n²) worst | Efficient |
| Counting Sort | O(n+k) | Linear |
| Heap Sort | O(n log n) | Efficient |

---

## 🧠 **10. Key Patterns and Intuition**

1. **If you’re halving input every iteration → `O(log n)`**
    
    ```python
    while n > 1:
        n //= 2
    
    ```
    
2. **If you’re looping over all elements → `O(n)`**
    
    ```python
    for i in arr:
        ...
    
    ```
    
3. **If you’re using two nested loops → `O(n²)`**
    
    ```python
    for i in arr:
        for j in arr:
            ...
    
    ```
    
4. **If recursive and splitting input in half → `O(n log n)`**
    
    (like merge sort, quick sort)
    

---

## 🧩 **11. Python Practice Examples**

### 🔹 Q1:

```python
for i in range(n):
    for j in range(i, n):
        print(i, j)

```

**Answer:**

Outer loop = n

Inner loop = (n - i) times

Total = n(n+1)/2 → **O(n²)**

---

### 🔹 Q2:

```python
i = 1
while i < n:
    for j in range(n):
        print(j)
    i *= 2

```

**Answer:**

Outer loop → log n

Inner loop → n

Total = **O(n log n)**

---

### 🔹 Q3:

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)

```

**Answer:**

Three nested loops → **O(n³)**

---

## 🧩 **12. Summary Table**

| Growth | Notation | Example | Performance |
| --- | --- | --- | --- |
| Constant | O(1) | Access element | ⚡ Excellent |
| Logarithmic | O(log n) | Binary Search | 🔥 Great |
| Linear | O(n) | Traverse list | ✅ Good |
| Linearithmic | O(n log n) | Merge Sort | ⚙️ Efficient |
| Quadratic | O(n²) | Nested loops | 🐢 Slow |
| Cubic | O(n³) | Triple loops | 🐌 Very slow |
| Exponential | O(2ⁿ) | Fibonacci recursion | 🚫 Impractical |
| Factorial | O(n!) | Permutations | ❌ Impossible for large n |

---

## 🧭 **13. Visualization — Growth Comparison**

| Input (n) | O(1) | O(log n) | O(n) | O(n log n) | O(n²) |
| --- | --- | --- | --- | --- | --- |
| 10 | 1 | 3 | 10 | 33 | 100 |
| 100 | 1 | 7 | 100 | 664 | 10,000 |
| 1,000 | 1 | 10 | 1,000 | 10,000 | 1,000,000 |

📈 As `n` grows, slow algorithms explode in time.
