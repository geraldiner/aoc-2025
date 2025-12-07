import math 
FILE_NAME = "input.txt"
PART_NUMBER = 2

def get_grand_total(lines):
  lists = []
  for line in lines:
    splits = line.split(" ")
    filtered = [s for s in splits if len(s) > 0]
    lists.append(filtered)
  grouping = [[] for _ in range(len(lists[0]))]
  for list in lists:
    for i, el in enumerate(list):
      grouping[i].append(el)
  total = 0
  for group in grouping:
    sign = group[-1]
    group_total = 0 if sign == '+' else 1
    for el in group[:-1]:
      if sign == '+':
        group_total += int(el)
      elif sign == '*':
        group_total *= int(el)
    total += group_total
  return total

def get_grand_total_2(lines):
  total = 0
  data = list(filter(bool, lines))
  op, nums = None, []
  for row in zip(*data):
    row = "".join(row).strip()
    print(row)
    if not row:
      total += sum(nums) if op == "+" else math.prod(nums)
      op, nums = None, []
    else:
      if op is None:
        row, op = row[:-1], row[-1]
      nums.append(int(row))
  total += sum(nums) if op == "+" else math.prod(nums)
  return total




# 4277556
# 5381996914800
if PART_NUMBER == 1:
  with open(FILE_NAME, 'r') as file:
    lines = file.readlines()
    print("Part 1:", get_grand_total([l.strip() for l in lines]))

# 3263827
# 9627174150897
if PART_NUMBER == 2:
  with open(FILE_NAME, 'r') as file:
    lines = file.readlines()
    print("Part 2:", get_grand_total_2(lines))
