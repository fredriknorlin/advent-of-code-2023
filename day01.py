import re
digits = [int(digit[0] + digit[-1]) 
    for digit in [re.findall(r'\d', line) for line in open('inputs/day01.txt')]]
print('part 1:', sum(digits))
