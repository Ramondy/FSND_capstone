# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask import jsonify, request, abort
from models import *

# ----------------------------------------------------------------------------#
# Helpers.
# ----------------------------------------------------------------------------#


# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    setup_db(app)
    migrate = Migrate(app, db)

    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE')
        return response

    @app.route('/', methods=['GET'])
    def health_check():
        return jsonify("Healthy"), 200

    # NOT USEFUL UNDER CURRENT SCOPE
    @app.route('/users', methods=['GET'])
    def get_users():
        users = User.query.all()
        users = [user.format() for user in users]
        return jsonify(users)

    # a Contributor can get details of his pledges
    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_user_details(user_id):
        selection_user = User.query.filter(User.id == user_id).one_or_none()

        if selection_user is not None:

            return jsonify({
                'success': True,
                'user_details': selection_user.format()
            }), 200

        else:
            abort(404)

    # a Fundraiser creates a Money_pot to raise money
    @app.route('/money_pots', methods=['POST'])
    def post_money_pot():
        data = request.get_json()
        title = data.get('title', None)
        description = data.get('description', None)
        target = data.get('target', 0)
        owner_id = data.get('owner_id', None)

        if (title is not None) & (owner_id is not None):
            target = int(target)
            owner_id = int(owner_id)

            try:

                new_money_pot = MoneyPot(title=title, description=description, target=target, owner_id=owner_id)
                new_money_pot.insert()

                return jsonify({
                    'success': True,
                    'money_pot_id': new_money_pot.id
                }), 200

            except:
                abort(500)

        else:
            abort(400)

    # the list of all Money_pots is accessible to both Fundraisers and Contributors
    @app.route('/money_pots', methods=['GET'])
    def get_money_pots():
        money_pots = MoneyPot.query.all()

        if money_pots is not None:

            money_pots = [money_pot.format() for money_pot in money_pots]

            return jsonify({
                "success": True,
                "money_pots": money_pots
            }), 200

        else:
            abort(404)

    # a Fundraiser can get details of all pledges for a Money_pot
    @app.route('/money_pots/<int:money_pot_id>', methods=['GET'])
    def get_money_pot_details(money_pot_id):

        selection_money_pot = MoneyPot.query.filter(MoneyPot.id == money_pot_id).one_or_none()
        if selection_money_pot is not None:

            selection_pledges = [pledge.format() for pledge in selection_money_pot.pledges]
            return jsonify({
                "success": True,
                "money_pot_id": money_pot_id,
                "money pot": selection_money_pot.format(),
                "pledges": selection_pledges
            }), 200

        else:
            abort(404)

    # a Fundraiser updates or deletes a Money_pot at will
    @app.route('/money_pots/<int:money_pot_id>', methods=['PATCH'])
    def patch_money_pot(money_pot_id):
        data = request.get_json()
        title = data.get('title', None)
        description = data.get('description', None)
        target = data.get('target', None)
        status = data.get('status', None)

        selection = MoneyPot.query.filter(MoneyPot.id == money_pot_id).one_or_none()

        if selection is not None:
            if title is not None:
                selection.title = title

            if description is not None:
                selection.description = description

            if target is not None:
                selection.target = target

            if status is not None:
                selection.status = status

            selection.update()

            return jsonify({
                "success": True,
                "money_pot_id": money_pot_id
            }), 200

        else:
            abort(404)

    # a Fundraiser updates or deletes a Money_pot at will
    @app.route('/money_pots/<int:money_pot_id>', methods=['DELETE'])
    def delete_money_pot(money_pot_id):

        selection = MoneyPot.query.filter(MoneyPot.id == money_pot_id).one_or_none()

        if selection is not None:
            try:
                selection.delete()

                return jsonify({
                    "success": True,
                    "money_pot_id": money_pot_id
                }), 200

            except:
                abort(500)

        else:
            abort(404)

    # a Contributor pledges money to any Money_pot
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

            try:
                new_pledge = Pledge(user_id=user_id, money_pot_id=money_pot_id, amount=amount)
                new_pledge.insert()

                return jsonify({
                    'success': True,
                    'pledge_id': new_pledge.id
                }), 200

            except:
                abort(500)

        else:
            abort(400)

    # ----------------------------------------------------------------------------#
    # Error handlers.
    # ----------------------------------------------------------------------------#

    @app.errorhandler(400)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request."
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource not found."
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Server error."
        }), 500

    return app

app = create_app()

# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#

# if __name__ == '__main__':
#     app = create_app()
#     app.run(host='127.0.0.1', port=8080, debug=True)