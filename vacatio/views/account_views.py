from flask import Blueprint
from flask import render_template

from vacatio.models import Account

bp = Blueprint('account', __name__, url_prefix='/account')


@bp.route('/')
def list():
    l_accounts = Account.query.order_by(Account.create_date.desc())
    return render_template(
                            'account/account_list.html',
                            l_accounts=l_accounts)


@bp.route('/add')
def add():
    l_accounts = Account.query.order_by(Account.create_date.desc())
    return render_template(
                            'account/account_list.html',
                            l_accounts=l_accounts)


@bp.route('/info/<int:account_id>')
def info():
    s_account = Account.query.get(account_id)
    return s_account
