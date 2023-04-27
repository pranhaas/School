word = input("Please enter the word\n").lower()
vowles = ["a","e","i","o","u"]
x = []

def converter(word):
    count = 0
    for n in word:
        x.append(n)
    for n in x:
        for y in vowles:
            if n==y:
                count +=1
    print(count)
    
    print(x)
converter(word)
    
