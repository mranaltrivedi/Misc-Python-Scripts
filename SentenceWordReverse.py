'''Reversing a sentence'''
#Reverses a sentence
def master_yoda(text):
    sentence = text.split()
    i = len(sentence)
    sentence_reversed = []
    for n in range(i-1,-1,-1):
        sentence_reversed.append(sentence[n])
    return " ".join(sentence_reversed)

print(master_yoda('This is Sparta'))
'''Reversing ends'''

'''Lesser of 2 evens'''
#Prints the lesser number if both numbers are even, else prints the greater number
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            return a
        elif b<a:
            return b
        else:
            return 'N/A'
    else:
        if a>b:
            return a
        elif b>a:
            return b
        else:
            return 'N/A'

print(lesser_of_two_evens(45,78))
'''Lesser of 2 evens ends'''

'''Returns True of first letters are the same for Two word strings'''
#for two-word strings
def animal_crackers(text):
    words = text.split()
    if words[0][0] == words[1][0]:
        return True
    else:
        return False

print(animal_crackers('Fort Bragg'))
'''Two words strings ends'''