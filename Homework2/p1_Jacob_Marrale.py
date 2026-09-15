# homework 2

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
def main():



if __name__ == "__main__":
    main()