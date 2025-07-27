
#! __name__ in shopping/sales.py and print initialization of modules
# ? __name__ in each file is equal to __main__ if the file is executed as a script.
# ? If the file is imported, __name__ is equal to the module name.

# from ecommerce.shopping import sales

#! sys, dir() , and file attributes

# import sys
# print(sys.path)
# from ecommerce.shopping import sales

# print(dir(sales))
# print(sales.__name__)
# print(sales.__package__)
# print(sales.__file__)


#! Importing modules
# # * ./modules/sales.py
# from ecommerce.shopping.sales import calc_tax, calc_shipping
# from ecommerce.sales as sales
# # * ./sales.py
# # from sales import calc_tax, calc_shipping

# import sales

# calc_shipping()
# calc_tax()
# print("--------- sales dot notation ---------")
# sales.calc_shipping()
# sales.calc_tax()
