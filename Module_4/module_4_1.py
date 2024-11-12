from fake_math import divide as fake_divide
from true_math import divide as true_divide


result1 = fake_divide(69, 3)
result2 = fake_divide(69, 3)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(fake_divide(69, 3))
print(fake_divide(3, 0))
print(fake_divide(0, 5))
print(fake_divide(0, 0))
print(true_divide(49, 7))
print(true_divide(15, 0))
print(true_divide(0, 2))
print(true_divide(0, 0))
