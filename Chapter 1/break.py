#Find First number greator than 100 and divisiible by 17

x = 101

while x > 100:
    x += 1

    if x % 17 == 0:
        print ('', x , 'is the first number greator than 100 that is divisible by 17.')
        break
