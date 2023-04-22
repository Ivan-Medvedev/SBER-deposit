import datetime
import calendar
import json

from flask import request, current_app

from api.datamodel.deposit_payment import DepositPayment
from api.datamodel.deposit_terms import DepositTerms


def add_months(source_date: datetime.date, months: int) -> datetime.date:
    month = source_date.month - 1 + months
    year = source_date.year + month // 12
    month = month % 12 + 1
    day = min(source_date.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def calculate_deposit(terms: DepositTerms) -> list[DepositPayment]:
    return [*map(
        lambda period: DepositPayment(
            add_months(terms.date, period),
            terms.amount * (1 + terms.rate / 12 / 100) ** (period + 1)
        ),
        range(terms.periods)
    )]


def deposit():
    try:
        data = request.get_json()
        current_app.logger.debug(data)

        terms = DepositTerms(
            data['amount'],
            data['periods'],
            data['rate'],
            datetime.datetime.strptime(data['date'], '%d.%m.%Y')
        )

        result = {p.date.strftime('%d.%m.%Y'): p.amount for p in calculate_deposit(terms)}
        current_app.logger.debug(result)
        return json.dumps(result), 200

    except Exception as e:
        current_app.logger.exception(e)
        return f'"error": {e}', 400
