def calculate_salary(days, bid):
    if days == 22:
        return bid 
    elif days < 22:
        return bid * 0.7
    else:
        return bid * 1.3
    