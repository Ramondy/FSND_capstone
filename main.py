# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from flask import Flask, jsonify, request, abort
from models import *

# ----------------------------------------------------------------------------#
# Helpers.
# ----------------------------------------------------------------------------#


# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#

@app.route('/', methods=['GET'])
def health_check():
    return jsonify("Healthy")


# NOT USED BY APPLICATION AS CURRENTLY SCOPED
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users = [user.format() for user in users]
    return jsonify(users)


@app.route('/money_pots', methods=['GET'])
def get_money_pots():
    money_pots = MoneyPot.query.all()
    money_pots = [money_pot.format() for money_pot in money_pots]
    return jsonify(money_pots)


@app.route('/pledges', methods=['POST'])
def create_pledge():
    data = request.get_json()
    user_id = data.get('user_id', None)
    money_pot_id = data.get('money_pot_id', None)
    amount = data.get('amount', 0)

    if (user_id is not None) & (money_pot_id is not None):
        user_id = int(user_id)
        money_pot_id = int(money_pot_id)
        amount = int(amount)

        new_pledge = Pledge(user_id=user_id, money_pot_id=money_pot_id, amount=amount)
        new_pledge.insert()

        return jsonify({
            'success': True
        })

# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)