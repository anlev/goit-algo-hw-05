import timeit


# -------------------
# Knuth-Morris-Pratt (KMP) Algorithm
# -------------------
def compute_lps(pattern):
    """Compute the Longest Prefix Suffix (LPS) array for KMP."""
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """Return the index of the first occurrence of pattern in text using KMP."""
    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)
    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
        if j == m:
            return i - j
    return -1


# -------------------
# Rabin-Karp Algorithm
# -------------------
def polynomial_hash(s, base=256, modulus=101):
    """Return the polynomial hash of a string s."""
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1, modulus)
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(text, pattern):
    """Return the index of the first occurrence of pattern in text using Rabin-Karp."""
    m = len(pattern)
    n = len(text)
    if m == 0 or n < m:
        return -1

    base = 256
    modulus = 101
    pattern_hash = polynomial_hash(pattern, base, modulus)
    current_hash = polynomial_hash(text[:m], base, modulus)
    h_multiplier = pow(base, m - 1, modulus)

    for i in range(n - m + 1):
        if pattern_hash == current_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            current_hash = (current_hash - ord(text[i]) * h_multiplier) % modulus
            current_hash = (current_hash * base + ord(text[i + m])) % modulus
            if current_hash < 0:
                current_hash += modulus
    return -1


# -------------------
# Boyer-Moore Algorithm
# -------------------
def build_shift_table(pattern):
    """Create the shift table for the Boyer-Moore algorithm."""
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    """Return the index of the first occurrence of pattern in text using Boyer-Moore."""
    m = len(pattern)
    n = len(text)
    if m == 0 or n < m:
        return -1

    shift_table = build_shift_table(pattern)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + m - 1], m)
    return -1


# -------------------
# Benchmark
# -------------------
def measure_time(func, text, pattern, repetitions=100):
    """Measure execution time of a function using timeit."""
    return timeit.timeit(lambda: func(text, pattern), number=repetitions)


def main():
    files = ["task03_article01.txt", "task03_article02.txt"]
    patterns_exist = ["GPGPU", "Ricci"]
    patterns_fake = ["ASJFoasdnvasddav", "fakepattern"]

    for idx, file_name in enumerate(files):
        with open(file_name, encoding="utf-8") as f:
            text = f.read()

        exist_pattern = patterns_exist[idx]
        fake_pattern = patterns_fake[idx]

        # -------------------
        # Assertions for correctness
        # -------------------
        index_kmp_exist = kmp_search(text, exist_pattern)
        index_rk_exist = rabin_karp_search(text, exist_pattern)
        index_bm_exist = boyer_moore_search(text, exist_pattern)

        # Assert all algorithms find the same existing substring
        assert index_kmp_exist == index_rk_exist == index_bm_exist, \
            f"Mismatch on existing substring in {file_name}"

        # Assert all algorithms return -1 for non-existing substring
        index_kmp_fake = kmp_search(text, fake_pattern)
        index_rk_fake = rabin_karp_search(text, fake_pattern)
        index_bm_fake = boyer_moore_search(text, fake_pattern)
        assert index_kmp_fake == index_rk_fake == index_bm_fake == -1, \
            f"Mismatch on non-existing substring in {file_name}"

        # -------------------
        # Measure performance
        # -------------------
        print(f"\n{file_name}:")
        print("KMP exist:", measure_time(kmp_search, text, exist_pattern))
        print("KMP fake:", measure_time(kmp_search, text, fake_pattern))
        print("Rabin-Karp exist:", measure_time(rabin_karp_search, text, exist_pattern))
        print("Rabin-Karp fake:", measure_time(rabin_karp_search, text, fake_pattern))
        print("Boyer-Moore exist:", measure_time(boyer_moore_search, text, exist_pattern))
        print("Boyer-Moore fake:", measure_time(boyer_moore_search, text, fake_pattern))


if __name__ == "__main__":
    main()
