import re

mul_expr = r"mul\(\d+,\d+\)"
number_expr = r"\d+"

def execute_mul(mul: str):
    numbers = re.findall(number_expr, mul)
    return int(numbers[0])*int(numbers[1])

def main():
    muls = []
    with open("input.txt", "r") as input_file:
        muls = re.findall(mul_expr, input_file.read())
        
    total = 0
    for mul in muls:
        total += execute_mul(mul)
    print(total)

main()