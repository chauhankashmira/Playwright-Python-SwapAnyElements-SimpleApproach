
# Swap Elements in a List (Simple Python Approach)

This is a simple Python script that demonstrates how to swap two elements in a list using basic list indexing.

## 📝 Description

The script:

* Initializes a list of integers.
* Prints the original list.
* Swaps the elements at positions `3` and `5`.
* Prints the updated list after the swap.

## 📌 Code Explanation

```python
# Simple approach

mylist = [10, 20, 30, 40, 50, 60, 70]
print(mylist)

pos1, pos2 = 3, 5

mylist[pos1], mylist[pos2] = mylist[pos2], mylist[pos1]
print(mylist)
```

### Step-by-step:

1. **Original List:**
   `[10, 20, 30, 40, 50, 60, 70]`

2. **Swap Positions:**
   `pos1 = 3` (value: 40)
   `pos2 = 5` (value: 60)

3. **After Swap:**
   `[10, 20, 30, 60, 50, 40, 70]`

## ▶️ How to Run

Make sure you have Python installed, then run the script with:

```bash
python script_name.py
```

Replace `script_name.py` with the name you give to this file (e.g., `swap_list.py`).

## ✅ Output

```
[10, 20, 30, 40, 50, 60, 70]
[10, 20, 30, 60, 50, 40, 70]
```

## 💡 Notes

* This method is concise and leverages Python’s ability to swap variables in a single line.
* The positions are zero-indexed, meaning the first element is at index `0`.

