def separate_number(amount, separator=','):
    formatted_amount = str(amount)
    if len(formatted_amount) <= 3:
        return formatted_amount
    else:
        return separate_number(formatted_amount[:-3], separator) + separator + formatted_amount[-3:]
