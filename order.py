import os
import sys

product_file = "product.txt"
user_file = "user.txt"

def readproduct():
    if not os.path.exists(product_file):
        print("File does not exist")
        return {}

    with open(product_file, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    products = {}

    for i in range(0, len(lines), 3):
        product_id = lines[i].split(":")[1]
        product_name = lines[i+1].split(":")[1]
        product_price = int(lines[i+2].split(":")[1])  

        products[product_id] = {
            "name": product_name,
            "price": product_price
        }

    return products

def readuser():
    if os.path.exists(user_file):
        with open(user_file, "r") as file:
            lines = [line.strip() for line in file if line.strip()]
            data = {}

            for i in range(0, len(lines), 2):
                user_id = lines[i].split(":")[1]
                user_name = lines[i+1].split(":")[1]
                data[user_id] = user_name

            return data   
    else:
        print("File does not exist")
        return {}
    

# users =readuser()
# print(users)
# products = readproduct()
# print(products)

def create_order(users, products):
    order_file="order.txt"
    user_id = input("Enter User ID: ").upper()
    product_id = input("Enter Product ID: ").upper()
    quantity = int(input("Enter Quantity: "))

    # Check if user and product exist
    if user_id not in users:
        print("User not found!")
        return

    if product_id not in products:
        print("Product not found!")
        return

    #Generate Order ID

    order_number = 1
    prefix = f"{user_id}-{product_id}"
    
    user_name = users[user_id]
    product_name = products[product_id]["name"]

    if not os.path.exists(order_file) or os.stat(order_file).st_size==0:
        with open(order_file,"w") as file:
            file.write(f"Order_id:{prefix}-{order_number}\n")
            file.write(f"User_name:{user_name}\n")
            file.write(f"Product_name:{product_name}\n")
            file.write(f"Quantity:{quantity}\n\n")
    else:
        new_order_number = 1
        with open(order_file, "r") as file:
            for line in file:
                if line.startswith("Order_id"):
                    last_order_id = line.strip().split(":")[1]
                    if last_order_id.startswith(prefix):
                       new_order_number = int(last_order_id[-1])+1
        new_order_id = f"{prefix}-{new_order_number}"
        with open("order.txt", "a") as file:
            file.write(f"Order_id:{new_order_id}\n")
            file.write(f'User_name:"{user_name}"\n')
            file.write(f'Product_name:"{product_name}"\n')
            file.write(f'Quantity:"{quantity}"\n')
            file.write("\n")

    print("Order Created Successfully!")
def readorder():
    if os.path.exists("order.txt"):
        with open ("order.txt","r") as file:
            data = file.read()
            print(f"The order details:\n{data}")


def readorderbyid():
    target_id = input("Enter which id you want to serach: ").upper()
    found =False
    if os.path.exists("order.txt"):
        with open("order.txt","r") as file:
            lines = file.readlines()
            for i  in range(len(lines)):
                if lines[i].startswith("Order_id:"):
                    order_id = lines[i].strip().split(":")[1].strip()
                    
                    if order_id == target_id:
                        found = True
                        print("Id found")
                        print(lines[i])
                        print(lines[i+1])
                        print(lines[i+2])
                        print(lines[i+3])
                        break
        if not found:
            sys.exit("Id not found")
    else:
        print("file not found")
    

