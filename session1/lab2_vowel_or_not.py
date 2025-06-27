"""Write a Python program to test whether a passed letter is a vowel or not."""


def vowel(letter):
    """Write your solution here. Don't forget to return the result at the end."""
    # vowel_list = ['a', 'e', 'i', 'o', 'u']
    # if str(letter).isupper:
    #     print(letter + " is upper case") # prints a is upper case!
    #     return str(letter).lower in vowel_list
    # else:
    #     print(letter + " is lower case")
    #     return str(letter) in vowel_list
    return letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if __name__ == "__main__":
    assert vowel("a"), "Test case failed"
    assert not vowel("b"), "Test case failed"
    assert vowel("A"), "Test case failed"
    assert not vowel("B"), "Test case failed"
    assert vowel("e"), "Test case failed"
    assert vowel("E"), "Test case failed"
    assert vowel("i"), "Test case failed"
    assert vowel("I"), "Test case failed"
    assert vowel("o"), "Test case failed"
    assert vowel("O"), "Test case failed"
    assert vowel("u"), "Test case failed"
    assert vowel("U"), "Test case failed"
    assert not vowel("z"), "Test case failed"
    assert not vowel("Z"), "Test case failed"
