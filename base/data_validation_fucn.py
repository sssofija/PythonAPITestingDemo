from faker import Faker
import random
import string

fake = Faker()

def generate_valid_category():
    length = random.randint(1, 14)
    allowed_chars = string.ascii_letters + string.digits + '-'
    return ''.join(random.choices(allowed_chars, k=length))

def generate_invalid_category_with_underscore():
    return generate_valid_category() + "_"

def generate_random_string(length=15):
    return ''.join(random.choices(string.digits, k=length))

def generate_invalid_string(length=10, with_text=False, text_length=5):
    forbidden_chars = "@#$%^&*()_+=[]{}|;:,.<>?/~"
    if with_text:
        random_char = random.choice(forbidden_chars)
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=text_length))
        return f"{random_text}{random_char}"
    return ''.join(random.choices(forbidden_chars, k=length))

def generate_random_russian_uppercase_category(length=14):
    allowed_chars = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    length = random.randint(1, min(length, 14))
    return ''.join(random.choices(allowed_chars, k=length))

def generate_random_english_uppercase_category(length=14):
    allowed_chars = string.ascii_uppercase
    length = random.randint(1, min(length, 14))
    return ''.join(random.choices(allowed_chars, k=length))

def generate_random_english_russian_uppercase_category(length=14):
    allowed_chars = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ' + string.ascii_uppercase
    length = random.randint(1, min(length, 14))
    return ''.join(random.choices(allowed_chars, k=length))

def generate_random_russian_lowercase_category(length=14):
    allowed_chars = 'абвдеёжзийклмнопрстуфхцчшщэюя'
    length = random.randint(1, min(length, 14))
    return ''.join(random.choices(allowed_chars, k=length))

def generate_random_english_lowercase_category(length=14):
    allowed_chars = string.ascii_lowercase
    length = random.randint(1, min(length, 14))
    return ''.join(random.choices(allowed_chars, k=length))

def generate_random_english_russian_lowercase_category(length=14):
    allowed_chars = 'абвдеёжзийклмнопрстуфхцчшщэюя' + string.ascii_lowercase
    length = random.randint(1, min(length, 14))
    return ''.join(random.choices(allowed_chars, k=length))

def generate_random_english_mixed_case_category(length=14):
    allowed_chars = string.ascii_letters
    length = random.randint(1, min(length, 14))
    return ''.join(random.choices(allowed_chars, k=length))

def generate_random_russian_mixed_case_category(length=14):
    allowed_chars = 'абвдеёжзийклмнопрстуфхцчшщэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    length = random.randint(1, min(length, 14))
    return ''.join(random.choices(allowed_chars, k=length))

def generate_category_with_dash_at_start():
    category = generate_valid_category()
    return "-" + category

def generate_category_with_dash_in_middle():
    category = generate_valid_category()
    if len(category) < 2:
        return category
    middle_index = random.randint(1, len(category) - 1)
    return category[:middle_index] + "-" + category[middle_index:]

def generate_category_with_number_at_start():
    category = generate_valid_category()
    return str(random.randint(1, 9)) + category

