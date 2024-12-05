import re

mul_expr = r"mul\(\d+,\d+\)"
number_expr = r"\d+"
remove_sequences_expr = r"don't\(\).*?do\(\)"

def execute_mul(mul: str):
    numbers = re.findall(number_expr, mul)
    return int(numbers[0])*int(numbers[1])

def get_clean_file_content(file_content: str):
    # replace whitespace with x to make one single line
    file_content = re.sub(r"\s", "x", file_content)
    # remove sequences of don't()....do()
    file_content = re.sub(remove_sequences_expr, "", file_content)
    # find if there are any remaining don't()
    dont_index = file_content.find("don't()")
    # return content without don't()
    if dont_index != -1:
        return file_content[0:dont_index]
    return file_content

def main():
    file_content = ""
    with open("input.txt", "r") as input_file:
        file_content = get_clean_file_content(input_file.read())
        
    muls = re.findall(mul_expr, file_content)
    total = 0
    for mul in muls:
        total += execute_mul(mul)
    print(total)

main()