from secrets import choice
from string import ascii_letters, ascii_lowercase, ascii_uppercase, punctuation, digits

def new_key(length):
    return ''.join(choice(ascii_uppercase + ascii_lowercase + ascii_lowercase + punctuation + digits + ascii_letters) for _ in range(0, length))
