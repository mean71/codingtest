T = int(input())
for _ in range(T):
    dollar = int(input())
    quarter,dollar = dollar//25,dollar%25
    dime,dollar = dollar//10,dollar%10
    nickel,dollar = dollar//5,dollar%5
    penny = dollar
    print('{} {} {} {}'.format(quarter, dime, nickel, penny))