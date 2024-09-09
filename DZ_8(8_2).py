def is_palindrome(text):
    clean_text = []
    for char in text:
        if char.isalnum():
            clean_text.append(char.lower())
    return clean_text == clean_text[::-1]

# Тест
assert is_palindrome('A man, a plan, a canal: Panama') == True
assert is_palindrome('0P') == False
assert is_palindrome('a.') == True
assert is_palindrome('aurora') == False
assert is_palindrome('madam') == True


print("ОК")
