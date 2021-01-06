num1 = 24
num2 = 36

i = 24

while(True):

    
    if i % num1 == 0 and i % num2 == 0:
        break
    i += 1
    print ('The Least Common Multilpe of', num1 , 'and', num2 , 'is', i , '.')
