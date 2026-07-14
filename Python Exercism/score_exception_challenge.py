def clean_score_list(score_strings):
    new_list =[]
    if type(score_strings) != list:
        raise TypeError(f"score_strings must be a list")
    for score in score_strings:
        try:
            if type(score) == int and int(score) >= 0:
                new_list.append(score)
                print(new_list) 
            elif type(score) == str and int(score) >= 0:
                new_list.append(int(score))
                print(new_list)
        except ValueError:
            continue
    return new_list