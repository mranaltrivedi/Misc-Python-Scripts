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
