data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    num = 0
    for elem in data:
        if isinstance(elem, str):
            num += len(elem)
        elif isinstance(elem, int):
            num += elem
        elif isinstance(elem, dict):
            num += calculate_structure_sum(list(elem.items()))
        else:
            num += calculate_structure_sum(list(elem))
    return num


result = calculate_structure_sum(data_structure)
print(result)
