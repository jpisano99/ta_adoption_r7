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


class Bookings(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer(), primary_key=True)
    fiscal_year = db.Column(db.String(50))
    fiscal_quarter_id = db.Column(db.String(50))
    fiscal_period_id = db.Column(db.String(50))
    sales_level_1 = db.Column(db.String(50))
    sales_level_2 = db.Column(db.String(50))
    sales_level_3 = db.Column(db.String(50))
    sales_level_4 = db.Column(db.String(50))
    sales_level_5 = db.Column(db.String(50))
    sales_level_6 = db.Column(db.String(50))
    sales_agent_name = db.Column(db.String(50))
    email_id = db.Column(db.String(50))
    erp_sales_order_number = db.Column(db.String(50))
    web_order_id = db.Column(db.String(50))
    erp_end_customer_name= db.Column(db.String(50))
    end_customer_global_ultimate_name = db.Column(db.String(50))
    end_customer_global_ultimate_id = db.Column(db.String(50))
    tms_level_2_sales_allocated = db.Column(db.String(50))
    product_family = db.Column(db.String(50))
    bundle_product_id = db.Column(db.String(50))
    product_id = db.Column(db.String(50))
    tms_sales_allocated_product_bookings_net = db.Column(db.Float)
    tms_sales_allocated_service_bookings_net = db.Column(db.Float)
    # hash_value = db.Column(db.String(50), primary_key=True)
    # date_added = db.Column(db.DateTime)


# class Customers(db.Model):
#     __tablename__ = 'customers'
#
#     id = db.Column(db.Integer(), primary_key=True)
#     last_name = db.Column(db.String(45))
#     first_name = db.Column(db.String(45))
