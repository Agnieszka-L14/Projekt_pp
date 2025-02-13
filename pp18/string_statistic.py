

def count_letters(string):
    stats = {}
    for letter in string:
        stats[letter] = stats.get(letter, 0) + 1
    return stats

 print(count_letters('abc'))