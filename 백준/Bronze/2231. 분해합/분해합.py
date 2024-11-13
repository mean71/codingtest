x = input()

for i in range(1,int(x)):
    if sum(map(int,str(i)))+i == int(x):
        print(i)
        break
else:
    print("0")