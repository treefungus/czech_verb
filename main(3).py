def verb(inf):
    sg = ["ám", "áš", "á"]

'''
x = word.split("at")
print(x)

y = word.index("at")
print(y)
        
z = "at"
print(z in word)

root = word.strip("at")
print(root)
'''

word = input("zadej sloveso: ")
sg = ["ám", "áš", "á"]
pl = ["áme", "áte", "ají"]
ends = ["at", "it"]
x = "at"

if x in word:
    conj1 = word.replace(x, sg[0])
    conj2 = word.replace(x, sg[1])
    conj3 = word.replace(x, sg[2])
    
    conj4 = word.replace(x, pl[0])
    conj5 = word.replace(x, pl[1])
    conj6 = word.replace(x, pl[2])
    
    print(conj1)
    print(conj2)
    print(conj3)
    
    print(conj4)
    print(conj5)
    print(conj6)

