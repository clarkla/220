"""
Name: Luke Clark
sales_person.py

Problem: This file creates a sales person class based on their name and employee id,
it also allows adding and comparing of sales

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    """Creates SalesPerson object"""
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(float(sale))

    def get_sales(self):
        return self.sales

    def total_sales(self):
        return sum(self.sales)

    def met_quota(self, quota):
        return self.total_sales() >= quota

    def compare_to(self, other):
        value = None
        if self.total_sales() < other.total_sales():
            value = -1
        if self.total_sales() > other.total_sales():
            value = 1
        if self.total_sales() == other.total_sales():
            value = 0
        return value

    def __str__(self):
        return "{}-{}:{}".format(self.employee_id, self.name, self.total_sales())
