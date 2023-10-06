
# ahmed-mini-project

# Week1

Week1 consists of a while loop and five simple if/elif loops. which print a product in a list gives the user the option to view list of products, insert a new product, alter an existing products name or delete a product.

# Week2

introduces order menu, each order consists of customer name, customer address, customer phone number and the status of the order.
The orders are stored in a list of dictionaries. 

The user can view the orders list.

The user can then input a new order. input username, customer address, customer phone number and the status are automatically set to preparing.

The user can alter the status of the order. 

The user can alter an existing order such as change the name address, phone number of an existing order from the list of orders.

The user can also delete the order.

# Week3 

so, with week 3, we now have three menus a products menu, orders menu, and a couriers menu. Where orders menu is option 1 couriers’ menu is option 2 is the couriers’ menu and option 3 is the orders menu.

option one is just reusing the code from week 1, option 2 is the new menu for couriers, option 3 is the orders menu.

option 1 runs the same as it did in week one with the only difference being that it utilises text files. The data in the list of products is imported from a text file and when the user edits the app the products list is saved back into the list.

option 2 is the courier menu, which lets the user create a new courier which is just a name insert, lets the user view the courier menu the user can edit an existing courier or delete an existing courier.

option 3 is the orders menu operate exactly as the week before but now, each order is assigned a courier and the user can now view as part of the order or alter the order details including the courier. 

# Week4 

so, for all products, couriers and orders the data for each field is now imported from a csv and stored in csv when the app is existed. 

Options 1 and 2 operate the same as the previous week.

Option3 the orders area now has a new feature in which each order has a items segment which is a list of items from the products list. in new orders the user can assign the items they want, and when they edit an order, they can add items to an existing order or start from scratch.

# Week5

week 5 the mini app works the same, but this time data is being imported and exported from a MYSQL database. the same features but imported and exported from MySQL database.

# where-have-you-bean
ETL project. CSV sales dataset is first inserted into AWS S3 bucket, this triggers a lambda function for data extraction. The data is then transformed into normalized tables, loaded into Amazon redshift and established a connection to Grafana for versatile data visualization.

