import string

def count_consonants(text):
    count = 0
    text = [str(i) for i in text.lower()]
    consonants = []
    for i in text:
        i = i.lower()
        # remove all the vowels
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            pass
        elif i in string.punctuation:
            pass
        elif i in string.digits:
            pass
        elif i == ' ':
            pass
        else:
            # ensure there are no duplicates, then create a consonant list of unique character
            if i not in consonants:
                consonants.append(i)
                count += 1

    return count

import string
def count_consonants(text):
    consonants = {i
                  for i in string.ascii_lowercase
                  if i not in 'aeiou'}

    # return len({i for i in text.lower() if i in consonants})

    return len(consonants.intersection(text.lower()))



if __name__ == "__main__":
    text = 'Count my unique consonants!!'
    print(count_consonants(text))