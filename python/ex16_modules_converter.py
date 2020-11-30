def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


def find_max(user_list):
    max_num = 0
    for item in user_list:
        if item > max_num:
            max_num = item

    return max_num


