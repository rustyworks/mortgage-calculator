def calculate_monthly_payment(
        house_value, down_payment,
        interest_in_percents, periodic_in_years):
    total_payment = 0
    try:
        loan = house_value - down_payment
        interest_in_percents_permonth = interest_in_percents / 12 / 100
        periodic_in_months = periodic_in_years * 12
        total_payment = loan * \
                (interest_in_percents_permonth * (1 + interest_in_percents_permonth) ** periodic_in_months) / \
                (((1 + interest_in_percents_permonth) ** periodic_in_months) - 1)
    except:
        pass
    return round(total_payment)
