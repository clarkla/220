"""
Name: Luke Clark
sales_force.py

Problem: This file creates a sales force class encapsulating multiple SalesPerson
classes from a file.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from sales_person import SalesPerson


class SalesForce:
    """Creates SalesForce object"""
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        with open(file_name, "r") as file:
            for i in file:
                split_line = i.split(",")
                sales = split_line[2].split()
                self.sales_people.append(SalesPerson(int(split_line[0]), (split_line[1])[1:]))
                for sale in sales:
                    self.sales_people[-1].enter_sale(float(sale))

    def quota_report(self, quota):
        report = []
        for i in self.sales_people:
            temp = [int(i.get_id()), i.get_name(), float(i.total_sales()), i.met_quota(quota)]
            report.append(temp)
        return report

    def top_seller(self):
        top = []
        current_top = 0
        for i in self.sales_people:
            if i.total_sales() > current_top:
                current_top = i.total_sales()
        for i in self.sales_people:
            if i.total_sales() == current_top:
                top.append(i)
        return top

    def individual_sales(self, employee_id):
        for i in self.sales_people:
            if i.get_id() == employee_id:
                return i
        return None
