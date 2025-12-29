# Performance Analysis of Substring Search Algorithms

This document summarizes the performance of three substring search algorithms—**Knuth-Morris-Pratt (KMP)**, **Rabin-Karp**, and **Boyer-Moore**—on two text files: `task03_article01.txt` and `task03_article02.txt`. Each algorithm was tested with an **existing substring** and a **non-existing substring**, and execution times were measured over 100 repetitions.

---

## 1. Task03_Article01.txt

| Algorithm        | Existing Substring (s) | Non-existing Substring (s) |
|-----------------|-----------------------|----------------------------|
| KMP             | 0.0576                | 0.0645                     |
| Rabin-Karp      | 0.1452                | 0.1599                     |
| Boyer-Moore     | 0.0256                | 0.0094                     |

**Conclusion:**  
- **Existing substring:** Boyer-Moore is the fastest.  
- **Non-existing substring:** Boyer-Moore is the fastest.  
- **Overall:** Boyer-Moore outperforms KMP and Rabin-Karp for this text.

---

## 2. Task03_Article02.txt

| Algorithm        | Existing Substring (s) | Non-existing Substring (s) |
|-----------------|-----------------------|----------------------------|
| KMP             | 0.0739                | 0.0869                     |
| Rabin-Karp      | 0.2097                | 0.2314                     |
| Boyer-Moore     | 0.0371                | 0.0193                     |

**Conclusion:**  
- **Existing substring:** Boyer-Moore is the fastest.  
- **Non-existing substring:** Boyer-Moore is the fastest.  
- **Overall:** Boyer-Moore consistently performs better than KMP and Rabin-Karp on this text.

---

## 3. General Observations

1. **Boyer-Moore** consistently demonstrates the fastest search times, especially for non-existing substrings, due to its efficient shift heuristics.  
2. **KMP** is slower than Boyer-Moore but faster than Rabin-Karp in most cases.  
3. **Rabin-Karp** is the slowest overall due to hash computation overhead.  
4. Performance differences are more pronounced in longer texts and for non-existing substrings.

---

## 4. Recommendation

For **general-purpose substring search in large texts**, **Boyer-Moore** is recommended for its superior performance.  
**KMP** can be preferred if pattern preprocessing is acceptable and repeated searches are needed.  
**Rabin-Karp** is useful when searching for multiple patterns simultaneously or when rolling hash features are needed (e.g., plagiarism detection).
