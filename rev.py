def reversed_words():
    a = input("enter any word that you want to reverse: ")
    b = a.split()
    reverse = b[::-1] 
    print(reverse)
reversed_words()