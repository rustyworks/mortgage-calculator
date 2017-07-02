from flask import Blueprint, redirect, render_template, request, url_for


home_blueprint = Blueprint('home', __name__, template_folder='templates')


@home_blueprint.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            house_value = int(request.form.get('house_value'))
            down_payment = int(request.form.get('down_payment'))
            interest_in_percents = int(request.form.get('interest'))
            periodic_in_years = int(request.form.get('periodic'))
        except (ValueError, TypeError):
            return render_template('home/index.html'), 400

        monthly_payment = _calculate_monthly_payment(
                house_value=house_value,
                down_payment=down_payment,
                interest_in_percents=interest_in_percents,
                periodic_in_years=periodic_in_years)
        total_payment = monthly_payment * 12 * periodic_in_years

        return render_template('home/index.html', total_payment=_format_to_currency(total_payment), monthly_payment=_format_to_currency(monthly_payment))
    else:
        return render_template('home/index.html')

def _calculate_monthly_payment(house_value, down_payment, interest_in_percents, periodic_in_years):
    total_payment = 0
    try:
        loan = house_value - down_payment
        interest_in_percents_permonth = interest_in_percents / 12 / 100
        periodic_in_months = periodic_in_years * 12
        total_payment = loan * (interest_in_percents_permonth * (1 + interest_in_percents_permonth) ** periodic_in_months) / (((1 + interest_in_percents_permonth) ** periodic_in_months) - 1)
    except:
        pass
    return round(total_payment)

def _format_to_currency(amount, separator=','):
    formatted_amount = str(amount)
    if len(formatted_amount) <= 3:
        return formatted_amount
    else:
        return _format_to_currency(formatted_amount[:-3], separator) + separator + formatted_amount[-3:]
