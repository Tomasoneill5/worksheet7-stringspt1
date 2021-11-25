string= input('enter a word: ')

lastCharacter= len(string)-1
print("lastChar",lastCharacter)

stringReversed=string[lastCharacter::-1]
print(stringReversed)
if string==stringReversed:
    print('This is a palindrome')
else:
    print('This is not a palindrome')


'''
## another way
palindrome= True

for ch in range(0,len(string)):
    ch1 = string[ch]
    print(ch1)
    ch2=string[lastCharacter-ch]
    print(ch2)
    if ch1!=ch2:
        palindrome= False
        break
    
if palindrome== True:
    print('This is a palindrome')
else:
    print('This is not a palindrome')

'''





