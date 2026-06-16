import string

punctuation = string.punctuation

def Disc(a, b, c) -> tuple: 
    if a == 0:
        return None
        
    d = b**2 - 4 * a * c
    if d > 0:
        x_1 = (-b + d**0.5) / (2 * a)
        x_2 = (-b - d**0.5) / (2 * a)
        return (x_1, x_2)
    elif d == 0:
        return -b / (2 * a)
    else:
        return None




""" print(Disc(1, 3, 2)) """

def reder(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        test = file.read().lower()
    translator = str.maketrans('', '', string.punctuation)
    words = test.translate(translator).split()
    return words  

def is_anagram(w1, w2):
    return sorted(w1) == sorted(w2)

def anagrams(words):
    anagrams_text = {}
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            w1 = words[i]
            w2 = words[j]
            if w1 == w2:
                continue
            if is_anagram(w1, w2):
                if w1 not in anagrams_text:
                    anagrams_text[w1] = []
                if w2 not in anagrams_text[w1]:
                    anagrams_text[w1].append(w2)
                
    final_text = {}
    for key, val_list in anagrams_text.items():
        final_text[key] = ", ".join(val_list)
        
    return final_text

def result_write(final_text):
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(str(final_text))
    print('файл создан!')


def main():
    text = reder('text.txt')
    itog_text = anagrams(text)
    result_write(itog_text)

