x=int(input())
y=int(input())
if y > 0 and x > 0:
    print('1')
elif y > 0 and x < 0:
    print('2')
elif y < 0 and x > 0:
    print('4')
elif y < 0 and x < 0:
    print('3')