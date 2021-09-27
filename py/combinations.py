def combinations(*ints):
    prod = 1
    for n in ints:
        prod *= n if n else 1
    return prod
