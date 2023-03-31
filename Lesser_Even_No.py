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
