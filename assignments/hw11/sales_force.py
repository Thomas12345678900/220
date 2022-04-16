"""
Name: Thomas Scola
hw11.py
Problem: using classes to determine the top seller
Certification of Authenticity:
I received help from the CSL.
"""

from hw11.sales_person import SalesPerson

class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, 'r')
        data = file.readlines()
        for person in data:
            person_list = person.split(', ')
            person_id = int(person_list[0])
            person_name = person_list[1]
            sales = person_list[2].split()
            sales_person = SalesPerson(person_id, person_name)
            for sale in sales:
                sales_person.enter_sales(float(sale))
            self.sales_people.append(sales_person)

    def quota_report(self, quota):
        return_list = []
        for person in self.sales_people:
            return_list.append(person.get_id())
            return_list.append(person.get_name())
            return_list.append(person.total_sales())
            return_list.append(person.met_quota(quota))

        return return_list


    def top_seller(self):
        best_seller_list = []
        best_sales = []
        for every_sale in self.sales_people:
            sales = every_sale.get_sales()
            sales.sort()
            a_best_sale = sales[-1]
            best_sales.append(a_best_sale)
            best_seller_list.sort()
        if best_sales[-1] > best_sales[-2]:
            for every_person in self.sales_people:
                if best_sales[-1] in every_person.get_sales():
                    best_seller_list.append(every_person)
                    return best_seller_list
        elif best_sales[-1] == best_sales[-2]:
            for every_person_two in self.sales_people:
                if best_sales[-1] in every_person_two.get_sales():
                    best_seller_list.append(every_person_two)
                if best_sales[-2] in every_person_two.get_sales():
                    best_seller_list.append(every_person_two)
                    return best_seller_list


    def individual_sales(self, employee_id):
        for individual in self.sales_people:
            if employee_id == individual.get_id():
                return individual

    def get_sale_frequencies(self):
        frequency_list = []
        for every_sale in self.sales_people:
            sales = every_sale.get_sales()
            frequency_list.append(sales)
        frequency = {}
        for every_frequency in frequency_list:
            for every_frequency_two in every_frequency:
                if every_frequency_two in every_frequency:
                    frequency[every_frequency_two] += 1
                else:
                    frequency[every_frequency_two] += 1
            return frequency




