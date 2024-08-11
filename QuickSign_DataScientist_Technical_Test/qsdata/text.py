"""Module containing some function for science processing."""

from unidecode import unidecode


def anagram_check(str1: str, str2: str) -> bool:
    """Check if two strings are anagram.

    Args:
        str1 : first string
        str2 : second string

    Returns :
        True if both strings ara anagram. False otherwise.

    Raises:
        ValueError: when inputs are not strings.
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Wrong inputs. Inputs should be strings.")

    return sorted(str1.lower()) == sorted(str2.lower())


def reverse_words(sentence: str) -> str:
    """Revers words of a sentence:

    Args:
        sentence : Sentence containing multiple words.

    Returns:
        Sentence with words inverted.

    Raises:
        ValueError: when inputs are not strings.

    """
    if not isinstance(sentence, str):
        raise ValueError("Wrong input. Input should be a string.")

    reverse_list = sentence.split()[::-1]
    reverse_sentence = " ".join(reverse_list)
    return reverse_sentence


def remove_vowels(text: str) -> str:
    """Remove all vowels in a text, including the ones with accents.

    Args:
        text : text to remove vowels from.

    Returns:
        Text without vowels.

    Raises:
        ValueError: when input is not a string.
    """
    if not isinstance(text, str):
        raise ValueError("Wrong input. Input should be a string.")

    vowels = "aeiouyAEIOUY"
    text_without_vowels = unidecode(text)
    for vowel in vowels:
        text_without_vowels = text_without_vowels.replace(vowel, "")
    return text_without_vowels


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome, ignoring spaces and case sensitivity.

    Args:
        text : text to check if it is a palindrome.

    Returns:
        True if text is a palindrome. False otherwise.

    Raises:
        ValueError: when input is not a string.
    """
    if not isinstance(text, str):
        raise ValueError("Wrong input. Input should be a string.")

    text = text.lower().replace(" ", "")
    return text == text[::-1]


def compress_string(text: str) -> str:
    """Compress a string by counting consecutive caracters.

    Args:
        text : string

    Returns:
        Compressed version of text.

    Raises:
        ValueError: when inputs are not strings or string contains numbers.
    """
    if not isinstance(text, str) or any(char.isdigit() for char in text):
        raise ValueError("Wrong Inputs!! the string should not contain numbers")

    if not text:
        return ""

    output = text[0]
    counter = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            counter += 1
        else:
            output += str(counter) if counter > 1 else ""
            counter = 1
            output += text[i]
    output += str(counter) if counter > 1 else ""
    return output


def uncompress_string(text: str) -> str:
    """Uncompress a string that was compressed by the compress_string function.

    Args:
        text : The compressed string.

    Returns:
        The original uncompressed version of the string.

    Raises:
        ValueError: when inputs are not strings.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    output = ""
    letter = ""
    count = ""

    for char in text:
        if char.isalpha() or char in r"!@#$%^&*()_+={}\[\]:;\"\'<>,.?/\\|`~ -":
            if count:
                output += letter * (int(count) - 1)
                count = ""
            letter = char
            output += char
        elif char.isdigit():
            count += char

    if count:
        output += letter * (int(count) - 1)

    return output
