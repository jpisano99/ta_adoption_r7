from my_app import db


class Test_Table(db.Model):
    __tablename__ = 'test_table'

    # Use this to specify a default schema/db for this table
    # __table_args__ = {'schema': 'dev'}

    # Us this to specify a different bind/sql server for this table
    # __bind_key__ = 'dev'

    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    qty_on_hand = db.Column(db.Integer)
    cost = db.Column(db.Float)
    date_added = db.Column(db.DateTime)
    password_hash = db.Column(db.String(128))

    @staticmethod
    def newest():
        return Test_Table.query.all()

    def newest_name(num):
        return Test_Table.query.order_by(Test_Table.first_name).limit(num)

    def __repr__(self):
       return "<name {}: '{} , {}'>".format(self.id, self.pss_name,self.tsa_name)


# class Bookings(db.Model):
#     __tablename__ = 'bookings'
#
#     erp_end_customer_name = db.Column(db.String(100))
#     total_bookings = db.Column(db.Float)
#     product_id = db.Column(db.String(25))
#     date_added = db.Column(db.DateTime)
#     hash_value = db.Column(db.String(50), primary_key=True)


# class Customers(db.Model):
#     __tablename__ = 'customers'
#
#     id = db.Column(db.Integer(), primary_key=True)
#     last_name = db.Column(db.String(45))
#     first_name = db.Column(db.String(45))
