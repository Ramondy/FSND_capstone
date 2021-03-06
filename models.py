# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

# ----------------------------------------------------------------------------#
# Configuration: tying Flask App and SQLAlchemy
# ----------------------------------------------------------------------------#

db = SQLAlchemy()


def setup_db(app):
    db.app = app
    db.init_app(app)

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#


class User(db.Model):
    __tablename__ = 'users'

    # ATTRIBUTES
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String)
    email = Column(db.String)

    # RELATIONSHIPS
    money_pots = db.relationship('MoneyPot', backref='owner')
    pledges = db.relationship('Pledge', backref='contributor')

    # METHODS
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'user_id': self.id,
            'pledges': [pledge.format() for pledge in self.pledges]
        }


class MoneyPot(db.Model):
    __tablename__ = 'money_pots'

    # ATTRIBUTES
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    target = Column(Integer)
    pledge_total = Column(Integer)
    status = Column(String)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # RELATIONSHIPS
    pledges = db.relationship('Pledge', backref='money_pot')

    # METHODS
    def __init__(self, title, description, target, owner_id):
        self.title = title
        self.description = description
        self.target = target
        self.pledge_total = 0
        self.status = 'open'
        self.owner_id = owner_id

    def is_open(self):
        return self.status == 'open'

    def accept_pledge(self, amount):
        if self.is_open():
            self.pledge_total += amount
            # self.update()
            return {
                'success': True,
                'message': "Thank you for your pledge.",
                'id': self.id
            }
        else:
            return {
                'success': False,
                'message': "The Money Pot is closed."
            }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'target': self.target,
            'pledge_total': self.pledge_total,
            'status': self.status,
            'owner_id': self.owner_id
        }


class Pledge(db.Model):
    __tablename__ = 'pledges'

    # ATTRIBUTES
    id = Column(Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    money_pot_id = db.Column(db.Integer, db.ForeignKey('money_pots.id'))
    amount = db.Column(db.Integer)
    status = db.Column(db.String)

    # METHODS
    def __init__(self, user_id, money_pot_id, amount):
        self.user_id = user_id
        self.money_pot_id = money_pot_id
        self.amount = amount
        self.status = 'pending'

        self.submit_to_money_pot()

    def submit_to_money_pot(self):
        money_pot = MoneyPot.query.filter(MoneyPot.id == self.money_pot_id).one_or_none()

        if money_pot is not None:
            result = money_pot.accept_pledge(self.amount)

            if result['success']:
                self.status = 'posted'

            else:
                self.status = 'rejected'

            print(result['message'])

        else:
            print("This Money Pot does not exist.")

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'pledge_id': self.id,
            'user_id': self.user_id,
            'money_pot_id': self.money_pot_id,
            'amount': self.amount
        }
