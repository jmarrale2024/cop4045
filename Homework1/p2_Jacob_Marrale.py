import math

def find_Pythagorean(n):
    if n == 0:
        return []
    elif n < 0:
        return []

    n = n + 1

    result = [] # tuples within

    for i in range(n):
        for k in range (n):
            for j in range(n):

                big_three = (i,k,j)

                a = i**2
                b = k**2
                c = j**2   

                if a + b == c:
                    result.append(big_three)
    # filtered result tuples filter tuples with 0's
    filtered_result = [t for t in result if 0 not in t]   

    seen = set()
    deduplicated_result = []
    # deduplicate the tuples that share the same numbers but in a different order
    for item in filtered_result:
        key = frozenset(item)
        if key not in seen:
            seen.add(key)
            deduplicated_result.append(item)               
    
    return deduplicated_result



while True:

    n = int(input("Please give a positive integer: "))

    print(find_Pythagorean(n))
    break

