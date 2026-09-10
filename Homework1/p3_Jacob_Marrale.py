
def find_dup_str(s,n):
    # add condition for if s is < n then answer is 0
    if len(s) < n:
        return ""
    
    seperated_strings = [letter for letter in s]

    split_strings = []
    for i,string in enumerate(seperated_strings):
        check = seperated_strings[i:i+n]
        split_strings.append(check)
    # my splicing leaves an extra list with less than n values so remove it
    for spt in list(split_strings):
        if len(spt) != n:
            split_strings.remove(spt)

    # find the lists that match
    matches = [ls for i,ls in enumerate(split_strings) if ls in split_strings[:i]]
    
    
    if len(matches) == 0:
    #    print('""')
        return ""
    
    inner_list = matches[0]

    final = "".join(inner_list)
    # print(f'"{final}"')
    return final

def find_max_dups(s):
    # call find_dup_str with a for loop based on the length of the string then append each string in a list here ["abc": 3]
    # then return the biggest one
    all_strings = {}
    for i in range(len(s)):
        chk = find_dup_str(s,i)
        if chk != None:
            all_strings[chk] = i
    if all_strings == None:
    #    print('""')
        return ""

    biggest = max(all_strings, key=len)
    return biggest

while True:

    s = str(input("Please input string: "))
    n = int(input("Please input length of substring: "))

    
    print(find_dup_str(s,n))
    print("biggest one:")
    print(find_max_dups(s))
    break