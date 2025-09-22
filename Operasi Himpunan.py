U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
print("Operasi Himpunan:")
print(f"A ∪ B: {A.union(B)}")
print(f"A ∩ B: {A.intersection(B)}")
print(f"A - B: {A.difference(B)}")
print(f"B - A: {B.difference(A)}")
print(f"A Δ B: {A.symmetric_difference(B)}")