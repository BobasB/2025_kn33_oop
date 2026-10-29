def fun_with_if_else(x):
    result = "Zero"
    if x > 0:
        result = "Positive"
    
    if x < 0:
        result = "Negative"

    return result


def fun_with_if_only(x):
    # if без else: тест з x > 0 виконає всі рядки (line coverage 100%),
    # але перехід "умова хибна -> пропустити if" не виконається,
    # тому branch coverage покаже частково покритий рядок (BrPart).
    result = "Non-positive"
    if x > 0:
        result = "Positive"
    return result
