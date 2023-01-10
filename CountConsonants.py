import string

def consonant_count(s):
    lowercase = string.ascii_lowercase
    alphabet_list = [str(i) for i in lowercase]

    consonants = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in alphabet_list:
        if i in vowels:
            continue
        else:
            consonants.append(i)

    expanded_string = [str(i.lower()) for i in s]

    count = 0
    for i in expanded_string:
        if i in consonants:
            count += 1

    return count

s = 'aeiouAEIOUxyzaeiou'
print(consonant_count(s))