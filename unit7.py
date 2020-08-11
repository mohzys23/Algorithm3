alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 
test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]
def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d
    

e = "Mose"
def has_duplicates(e):
    x = histogram(e)
    for i in x:
        if x[i] > 1:
            return True
    return False
histogram(e)

for i in test_dups:
    if has_duplicates(i):
        print(i, "has duplicates letters")
    else:
         print(i, "has no duplicates") 

f = "Mos"
def missing_letters(f):
     x = histogram(f)
     for i in x:
         if x[i] > 1:
            return True
     return False 
histogram(f)

for i in test_miss:
    if i not in alphabet:
        print(i, "is missing letters")
    else:
        print(i, "uses all the letters")
