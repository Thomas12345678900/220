"""
Name: Thomas Scola
hw11.py
Problem: using classes to determine the top seller
Certification of Authenticity:
I received help from the CSL.
"""
class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = str(name)
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sales(self, sale_value):
        self.sales.append(sale_value)

    def total_sales(self):
        tot_sale = 0.0
        for every_sale in self.sales:
            tot_sale += every_sale

        return tot_sale

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        s = self.total_sales()
        o = other.total_sales()

        if o > s:
            return -1
        elif s > o:
            return 1
        elif o == s:
            return 0

    def __str__(self):
        return "{0}-{1}: {2}".format(self.employee_id, self.name, self.total_sales())



