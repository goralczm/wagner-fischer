from typing import Set, List, Tuple


def load_words() -> Set:
    with open('words.txt', 'r') as file:
        return {word.strip() for word in file.readlines()}


def wagner_fischer(s1, s2) -> int:
    len_s1, len_s2 = len(s1), len(s2)

    current_row = list(range(0, len_s1 + 1))
    for row_index in range(1, len_s2 + 1):
        previous_row, current_row = current_row, [row_index] + [0] * len_s1
        for col_index in range(1, len_s1 + 1):
            add, delete, change = previous_row[col_index], current_row[col_index - 1], previous_row[col_index - 1]
            curr = min(add, delete, change)
            if s1[col_index - 1] != s2[row_index - 1]:
                curr += 1

            current_row[col_index] = curr

    return current_row[len_s1]


def spell_check(word, words_set) -> List[Tuple]:
    if word in words_set:
        return [(word, 0)]

    suggestions = []

    for correct_word in words_set:
        distance = wagner_fischer(word, correct_word)
        suggestions.append((correct_word, distance))

    suggestions.sort(key=lambda x: x[1])
    return suggestions[:10]


words_set = load_words()
searching_word = 'wordd'

suggestions = spell_check(searching_word, words_set)

if suggestions[0] == (searching_word, 0):
    print("Correct word")
else:
    for word, distance in suggestions:
        print(f'Did you meant {word}?')
