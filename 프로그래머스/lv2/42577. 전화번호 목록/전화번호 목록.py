def solution(phone_book):
    phone = sorted(phone_book)
    for num1, num2 in zip(phone, phone[1:]):
        if num2.startswith(num1):
            return False
    return True