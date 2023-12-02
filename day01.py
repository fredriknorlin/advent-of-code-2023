import re
digits = [int(digit[0] + digit[-1]) 
    for digit in [re.findall(r'\d', line) for line in open('inputs/day01.txt')]]
print('part 1:', sum(digits))

regex = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'
digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
digits = [int(digits.get(digit[0], digit[0]) + digits.get(digit[-1], digit[-1])) 
    for digit in [re.findall(regex, line) for line in open('inputs/day01.txt')]]
print('part 2:', sum(digits))
