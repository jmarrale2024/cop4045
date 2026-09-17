# homework 2
import os # I see no other way to test 1b
# question 1a function: line_number
def line_number(read_file: str , write_file: str) -> str: # read first file , write its line prefixed with line numbers for second
    try:
        with open(read_file, 'r') as file1:
            lines = file1.readlines() # would use generator here but question didn't require it so just gonna load it all at once
        with open(write_file, 'w') as file2:
            for i, line in enumerate(lines, start=1):
                file2.write(f"{i}: {line}")
                print(f"{i}: {line}") # track if I did it right
    except Exception as e:
        print(f"Function Failure: {e}")
        raise

# question 1b function: parse_functions:
def parse_functions(parse_file: str) -> tuple: # read file, find functions, make nested tuples ex: ((9, "mul", 'x,y', 'def mul(x,y):\n\tz = x * y\n\treturn z\n')) , comments and empty lines gone
    # tuples must be ordered alphabetically based on function name

    try: 
        hold_tuples = []
        with open(parse_file, 'r') as parse:
            lines = parse.readlines()
        for i, line in enumerate(lines, start=1):
            if not line.startswith('def '): 
                continue
            func_line_num = i
            func_name = line.split("def ")[1].split("(")[0].strip() # makes two lists, first one to split and get the right side then second to get the left side, then stripe to get rid of spaces
            func_para = line.split("(")[1].split(")")[0].strip() # same trick for parameters in the function
            # get the whole function into a string
            def_line = line.split('#')[0].rstrip()
            func_code = [def_line + '\n']
            for body_line in lines[i:]:
                code = body_line.split('#')[0].rstrip()
                if not code:
                    continue
                if not code.startswith((' ', '\t')):
                    break
                func_code.append(code + '\n')

            this_tuple = (func_line_num, func_name, func_para, ''.join(func_code))
            hold_tuples.append(this_tuple)

        print("Jacob Marrale , 23779685")        
        print(tuple(sorted(hold_tuples, key=lambda x: x[1])))
        return tuple(sorted(hold_tuples, key=lambda x: x[1]))
                        

                    
        
    except Exception as e:
        print(f"Function Failure: {e}")
        raise

def main():

    # question 1a test:
    line_number(__file__, __file__ + '.txt')

    # question 1b test:
    test_path = os.path.join(os.path.dirname(__file__), 'funs.py')
    parse_functions(test_path)


if __name__ == "__main__":
    main()