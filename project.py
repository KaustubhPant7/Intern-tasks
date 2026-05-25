import order
import UAP

choice =  int(input("Enter your choice:\n1. Product\n2. User\n3.Create Order\n4. Read order: "))
if choice == 1:
  ch  = int(input("Enter Your choice\n1. Writer data in product\n2. Read data from product file\n3. Read data using id \n4. Update data using id \n5. Delete product"))
  if ch ==1:
    UAP.product()
  elif ch == 2:
    UAP.readproduct()
  elif ch == 3:
    UAP.readproductbyid()
  elif ch == 4:
    UAP.update_product()
  elif ch == 5:
    UAP.deleteproduct()
  else:
    print("Invalid Choice!")



elif choice ==2:
  ch  = int(input("Enter Your choice\n1. Writer data in user\n2. Read data from user file\n3. Read data using id \n4. Update data using id \n5. Delete user"))
  if ch ==1:
    UAP.user()
  elif ch ==2:
    UAP.readuser()
  elif ch == 3:
    UAP.readuserbyid()
  elif ch == 4:
    UAP.update_user()
  elif ch == 5:
    UAP.deleteuser()
  else:
    print("Invalid Choice!")

elif choice ==3:
  users = order.readuser()
  print(users)
  products = order.readproduct()
  print(products)
  input = input("Do you want to create order Y/N").upper()
  if input == 'Y':
    order.create_order(users,products)
  elif input == 'N':
    print("--------")
  else:
    print("Invalid Input")

elif( choice ==4):
  choic = int(input("1. read order\n 2. serch order by id: "))
  if choic ==1:
    order.readorder()
  elif choic ==2:
    order.readorderbyid()




else:
  print("Invalid Choice!")