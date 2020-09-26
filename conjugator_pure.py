word = input("zadej sloveso: ")

conj_at = ["ám", "áš", "á", "áme", "áte", "ají"]
conj_it = ["ím", "íš", "í", "íme", "íte", "í"]
conj_ovat = ["uju", "uješ", "uje", "ujeme", "ujete", "ujou"]

ends = ["ovat", "at", "it", "et", "ět"]

# dictionary in progress
prdgm = {ends[0]: conj_ovat, ends[1]: conj_at, ends[2]: conj_it}

#pure conjugator
def conj(verb_cls):
    no = 0
    for i in prdgm[ends[verb_cls]]:
    	print(word.replace(ends[verb_cls], prdgm[ends[verb_cls]][no]))
    	no += 1

#pure ending decider, to be dried up
def is_end(verb_cls):
    return ends[verb_cls] in word and ends[verb_cls] not in word.strip(ends[verb_cls])
    	
# to distinguish -ovat from -at + function conjugation, driest
if is_end(0):
    conj(0)
    
elif is_end(1):
    conj(1)
    
elif is_end(2):
    conj(2)
    
else:
    print("not a verb")