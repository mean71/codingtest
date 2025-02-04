def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
# 비효율적
# def solution(phone_book):
#     phone_book = set(phone_book)
#     for num in phone_book:
#         for i in range(len(num)):
#             if num[:i] in phone_book:
#                 return False
#     return True