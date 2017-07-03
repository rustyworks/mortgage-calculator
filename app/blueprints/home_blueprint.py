from flask import Blueprint, redirect, render_template, request, url_for
from app.helpers.formatter import separate_number
from app.services.payment_services import calculate_monthly_payment


home_blueprint = Blueprint('home', __name__, template_folder='templates')


@home_blueprint.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            house_value = int(request.form.get('house_value'))
            down_payment = int(request.form.get('down_payment'))
            interest_in_percents = float(request.form.get('interest'))
            periodic_in_years = int(request.form.get('periodic'))
        except (ValueError, TypeError):
            return render_template('home/index.html'), 400

        monthly_payment = calculate_monthly_payment(
                house_value=house_value,
                down_payment=down_payment,
                interest_in_percents=interest_in_percents,
                periodic_in_years=periodic_in_years)
        total_payment = monthly_payment * 12 * periodic_in_years

        return render_template('home/index.html', total_payment=separate_number(total_payment), monthly_payment=separate_number(monthly_payment))
    else:
        return render_template('home/index.html')

