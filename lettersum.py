from get_lettersum_challenge_list import get_lettersum_list

def letter_sum(letters):
    base = ord("a") - 1
    sum = 0
    for letter in letters.lower():
        sum += (ord(letter) - base)

    return sum


def build_word_dictionary():
    list = get_lettersum_list()

    sum_dict = {}

    for word in list:
        sum = letter_sum(word)
        if sum in sum_dict:
            sum_dict[sum].append(word)
        else:
            sum_dict[sum] = [word]

    return sum_dict

def find_total_odd_lettersum_words():
    sum_dict = build_word_dictionary()

    total = 0
    for key in sum_dict:
        if key % 2 != 0:
            total += len(sum_dict[key])
    
    return total

def find_largest_number_of_words_with_same_sum():
    sum_dict = build_word_dictionary()

    largest_key = 0
    largest_total = 0

    for key in sum_dict:
        total = len(sum_dict[key])
        if  total > largest_total:
            largest_key = key
            largest_total = total
    
    return f'The sum {largest_key} is the most common sum with {largest_total:,d} occurrences'
    
sum = find_total_odd_lettersum_words()
largest_total = find_largest_number_of_words_with_same_sum()

print(sum)
print(largest_total)
