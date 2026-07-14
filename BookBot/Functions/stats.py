def sort_on(stat: tuple[str,int]):
    return stat[1]

def chars_dict_to_sorted_list(stats):
    sorted_stats={}
    sorted_stats = sorted(stats.items(), reverse=True, key=sort_on)
    return sorted_stats

def letter_stats(file_content):
    file= file_content.lower()
    stats = {}
    for letter in file:
        if letter in stats:
            stats[letter] += 1
        else:
            stats[letter] = 1
    # sorted_stats = chars_dict_to_sorted_list(stats)
    return stats


def count_words(file_content):
    num_words = 0
    for word in file_content.split():
        num_words += 1
    return num_words