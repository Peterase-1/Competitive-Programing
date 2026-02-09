k, n, w = map(int, input().split())

totCost = k * w * (w + 1) // 2

borrow = max(0, totCost - n)

print(borrow)
