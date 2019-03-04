from pizzapy import *

class Pizza:
  def __init__(self,customer,store,menu,order,card):
    self.customer = customer
    self.store = store
    self.menu = menu
    self.order = order
    self.card = card
    self.orderList = [];

  #TODO error handling
  def initCustomer(self):
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    email = input ("Email: ")
    number = input ("Phone number: ")
    address = input ("Address: ")
    print("\n")

    self.customer = Customer(firstName, lastName, email, number, address)

    return self.customer
  
  def printCustomer(self):
    print(self.customer)
    return

  def initOrder(self):
    self.store = StoreLocator.find_closest_store_to_customer(self.customer)
    self.printLocalStore()
    self.menu = self.store.get_menu()
    print("Starting order for your location....")
    self.order = Order.begin_customer_order(self.customer, self.store)

    return 

  def printLocalStore(self):
    print("Your local dominos is: \n")
    print(self.store)
    return


  # TODO have error handling for order
  # TODO make loop completely stop when done is entered
  #added functions
  def addtoOrder(self):
    search = ''
    while search != 'done':
      search = input("Search for item (Enter 'done' to exit): ")
      print("Search results for " + search)
      print("\n")
      self.menu.search(Name=search)
      print("\n")
      
      confirm = input("Would you like to add anything to your order? (y/n): ")
      if confirm == 'y':
        name = input('Enter the name of the item you would like to add (to keep track of order): ') 
        item = input('Enter the code of the item you would like to add: ')
        self.orderList.append(name)
        self.order.add_item(item)
    
    print(self.orderList)
    
    return

# # TODO print how much it costs
# def printOrder(self):
#   print("Here is your current order:")
#   for x in self.orderList

def obtainMethod(order):
  option = input("Carryout or Delivery (c/d): ")
  if option == 'c':
    order.changeToCarryout()

def initCard():
  card = input("Enter credit card number: ")
  exp = input("Enter expiration: ")
  security = input("Enter Security code: ")
  billing = input("Enter billing ZIP: ")

  card = CreditCard(card, exp, security, billing)

  return card


def main():

  thePizza = Pizza('','','','','')
  thePizza.initCustomer()
  thePizza.printCustomer()
  thePizza.initOrder()
  thePizza.addtoOrder()

  # #Get customer information
  # customer = initCustomer()

  # #Find local Dominos, get menu, and begin order
  # my_local_dominos, menu, order = initOrder(customer)

  # #Search for items from menu and add to order
  # order = addtoOrder(order, menu)
  # print("Here is your order: ")
  # print(order.data['Products'])

  # #Choose between pick up or delivery
  # order = obtainMethod(order)
  # print(order)

  # #Get credit card information
  # card = initCard()

  # # Uncomment these to actually place order

  # # order.place(card)
  # # my_local_dominos.place_order(order, card)

  # print("test")


if __name__== "__main__":
  main()