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

# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)