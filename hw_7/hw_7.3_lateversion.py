def has_more_than_n_unique_chars(text: str, n: int = 10) -> bool:
    unique_chars = set(text)
    return len(unique_chars) > n



def count_vowels(text: str) -> int:
    vowels = "aeiouаеєиіїоуюяAEIOUАЕЄИІЇОУЮЯ"
    return sum(1 for char in text if char in vowels)



def reverse_string(text: str) -> str:
    return text[::-1]


def is_palindrome(text: str) -> bool:
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]


sample_text = "HililiH"

print("Більше 10 унікальних символів?", has_more_than_n_unique_chars(sample_text))
print("Кількість голосних:", count_vowels(sample_text))
print("Перевернутий рядок:", reverse_string(sample_text))
print("Чи паліндром?", is_palindrome(sample_text))
