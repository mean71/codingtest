def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

def solution(phone_book):
    set_num = set(phone_book)
    for num in set_num:
        for i in range(len(num)):
            if num[:i] in set_num:
                return False
    return True