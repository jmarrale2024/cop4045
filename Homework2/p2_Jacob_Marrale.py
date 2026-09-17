# homework 2



def main():

    # question 2a:
    fours = [
        (a,b,c,d)
        for a in range(1,11)
        for b in range(1,11)
        for c in range(1,11)
        for d in range(1,11)
        if len({a,b,c,d}) == 4 and a**2 + b**2 == c**2 + d**2 # does distinct mean non duplicate tuples? palindrome tuples are gone with this but some with same elements, theres no example so I'll leave this
    ]
    print(fours)

    # question 2b:
    numb_leng_exam = ['One', 'SEVEN', 'three', 'two', 'Ten']
    numbers_length = [
        (i.lower(), len(i))
        for i in numb_leng_exam
        if len(i) < 5 
    ]
    print(numbers_length)

    # question 2c:
    names = ['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']
    names_formatted = [
        f'{name.split(" ")[0]} {name.split(" ")[1][0]}. {name.split(" ")[2]}'
        for name in names
    ]
    print(names_formatted)

    # question 2d:
    lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
    lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]

    pairs = [
        (one, two)
        for one in lst1
        for two in lst2
        if sorted(one.lower()) == sorted(two.lower())
    ]
    print(pairs)

    # question 2e:
    s = ['one', 'two', 'three']

    jackson = {
        i: len(i) for i in s
    }
    print(jackson)

    # question 2f:
    vowels = "aeiou"
    text = "Hello world"
    bowl = {
        i: j for i,j in enumerate(text) if j in vowels
    }
    print(bowl)

    print("Jacob Marrale , 23779685")

if __name__ == "__main__":
    main()