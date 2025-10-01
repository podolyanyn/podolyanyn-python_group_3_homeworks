import random, time

def i_sort(a, L, R):
    for i in range(L+1, R+1):
        x = a[i]
        j = i - 1
        while j >= L and a[j] > x:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x

def split_h(a, L, R):
    p = a[(L+R)//2]
    i, j = L, R
    while True:
        while a[i] < p: i += 1
        while a[j] > p: j -= 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

def qsort_cut(a, L, R, cut):
    while L < R:
        if R - L + 1 <= cut:
            i_sort(a, L, R)
            return
        m = split_h(a, L, R)

        if m - L < R - m:
            qsort_cut(a, L, m, cut)
            L = m + 1
        else:
            qsort_cut(a, m+1, R, cut)
            R = m

n = int(input("Скільки елементів? "))
cut = int(input("Cutoff (на якому перейти на вставки): "))
a = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]

print("До:", a[:12], "..." if n > 12 else "")
t0 = time.perf_counter()
qsort_cut(a, 0, n-1, cut)
t1 = time.perf_counter()
print("Після:", a[:12], "..." if n > 12 else "")
print(f"Час: {t1 - t0:.6f} с")