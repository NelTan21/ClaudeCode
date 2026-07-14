def filter_messages(messages):
    print(f"There are {len(messages)} messages in this list")
    print("==============================================")
    new_messages = []
    filtered_word_count = []
    for i in range (0, len(messages)):
        print(f"Words from message ({i + 1}):")
        while i < len(messages):
            list_of_messages = messages[i].split()
            print(list_of_messages)
            print(f"Counting words in message ({i+1})...")
            print(f"There are ({len(list_of_messages)}) words in message ({i + 1}).")
            filter_count = 0
            for word in range(len(list_of_messages) - 1 , -1, -1):
                print(f"Checking word ({word+1}) from message ({i + 1}): ({list_of_messages[word]})")
                if list_of_messages[word] == "dang":
                    print(f"Spotted the word (dang)...")
                    print(f"Removing the word ({list_of_messages[word]}) from message ({i+1})...")
                    list_of_messages.pop(word)
                    filter_count += 1
                    print(f"There are now {len(list_of_messages)} words in message ({i + 1}) after removing (dang)")
                    print(f"This is the new list of words in message ({i+1}): \n\t{list_of_messages}")
            filtered_word_count.append(filter_count)
            joined_messages = " ".join(list_of_messages)
            print(joined_messages)
            print("==============================================")    
            break
        new_messages.append(joined_messages)    
        print(new_messages) 
    return new_messages, filtered_word_count


"""
def filter_messages(messages):
    filtered_messages = []
    dang_counts = []

    for message in messages:
        words = message.split()
        good_words = []
        dangs = 0

        for word in words:
            if word == "dang":
                dangs += 1
            else:
                good_words.append(word)

        filtered_messages.append(" ".join(good_words))
        dang_counts.append(dangs)

    return filtered_messages, dang_counts
"""