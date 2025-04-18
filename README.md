# 🔢 Day-6: Majority Element II

This repository contains a Python implementation to identify **all elements** in an array that appear more than ⌊n/3⌋ times. The logic is an extension of the **Moore’s Voting Algorithm**. This is a part of the **GeeksforGeeks 160 Days DSA Challenge**.

---

## 📌 Problem Statement

Given an integer array of size `n`, find **all elements** that appear **more than n/3 times**. Return the result in **sorted order**.

---

## 🧠 Approach & Intuition

The problem is an extension of the **Boyer-Moore Majority Voting Algorithm**. In this case, there can be **at most two majority elements** that satisfy the condition (> n/3 times).

### 🔄 Steps:

1. **First Pass (Candidate Selection)**:
   - Maintain two potential candidates and their respective counters.
   - Use the Moore’s Voting concept to reduce counts when no match is found.

2. **Second Pass (Validation)**:
   - Count actual occurrences of both candidates.
   - Include them in the result if their frequency exceeds ⌊n/3⌋.

---
## ▶️ Sample Execution
```
arr = [2, 1, 5, 5, 5, 6, 6, 6, 6]
# Expected Output: [5, 6]
```
---

## ✅ Time & Space Complexity
Time Complexity: O(n)

Space Complexity: O(1)
---
## 🙌 Contribution
Curated with ❤️ by Vikash Joshi as part of a consistent DSA learning series. Stay tuned for more optimized patterns and insights.

⭐ Don’t forget to like, share, and star the repo if it helps in your coding journey.
