import os
import sys
# create
def user():
  file_name ="user.txt"
  f_name = input("Enter first name: ")
  l_name = input("Enter last name: ")
  prefix =f"{f_name[0].upper()}{l_name[0].upper()}"
  

# if file is empty and file size is zero
  if not os.path.exists(file_name) or os.stat(file_name).st_size ==0:
    with open(file_name,"w") as file:
      num =1
      file.write(f"User id:{prefix}{num}\n")
      file.write(f"User Name:{f_name} {l_name}\n\n")

# if file exist garxa ra data entry xa bhane
  else:
    with open(file_name,"r")as file:
      num = 1
      for line in file:
        if line.startswith("User id:"):
          last_id = line.strip().split(":")[1]
          if last_id.startswith(prefix):
            try:
              num = int(last_id[2:])+1
            except ValueError:
              pass
    userid = f"{prefix}{num}"
    with open(file_name,"a")as file:
      file.write(f"User id:{userid}\n")
      file.write(f"User Name:{f_name} {l_name}\n\n")
    print("User added", userid)

def product():
  file_name = "product.txt"
  product_name = input("Enter Product Name: ")
  product_price = int(input("Enter product Price: "))
  prefix = product_name[0].upper()
  if not os.path.exists(file_name) or os.stat(file_name).st_size ==0:
    num =1
    with open(file_name,"w") as file:
      file.write(f"Product Id:{prefix}{num}\n")
      file.write(f"Product Name:{product_name}\n")
      file.write(f"Product Price:{product_price}\n\n")

  else:
    with open (file_name,"r") as file:
      num = 1
      for line in file:
        if line.startswith("Product Id:"):
          last_id = line.strip().split(":")[1]
          if last_id.startswith(prefix):
            try:
              num = int(last_id[1:])+1
            except ValueError:
              pass
    product_id =   f"{prefix}{num}"       
    with open(file_name,"a") as file:
      file.write(f"Product Id:{product_id}\n")
      file.write(f"Product Name:{product_name}\n")
      file.write(f"Product Price:{product_price}\n\n")
    print("Product Added")

#read user
def readuser():
  file_name ="user.txt"
  if os.path.exists(file_name):
    with open(file_name,"r") as file:
      data = file.read()
      print(f"The user data is \n{data}")
  else:
   print("file not found")    

# read product
def readproduct():
  file_name = "product.txt"
  if os.path.exists(file_name):
    with open(file_name,"r") as file:
      data = file.read()
      print(f"product data\n{data}")
  else:
    print("file not found")   

# Read user by id
def readuserbyid():
  file_name ="user.txt"
  found = False
  target_id = input("Enter id which you want to search").upper()
  if os.path.exists(file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()

            for i in range(len(lines)):
                if lines[i].startswith("User id:"):
                    user_id = lines[i].strip().split(":")[1].strip()

                    if user_id == target_id:
                        found = True
                        print("ID Found")
                        print(lines[i].strip())
                        if i + 1 < len(lines):
                            print(lines[i + 1].strip())
                        break

        if not found:
            sys.exit("ID not found") 
  else:
    print("FIle not found")  

# read product by id
def readproductbyid():
  file_name="product.txt"
  found= False
  target_id = input("Enter which Id you want to search: ").upper()
  if os.path.exists(file_name):
    with open(file_name,"r") as file:
      lines = file.readlines()
      for i in range(len(lines)):
        if lines[i].startswith("Product Id:"):
          product_id = lines[i].strip().split(":")[1]

          if product_id == target_id:
            found = True
            print("Id found")
            print(lines[i])
            print(lines[i+1])
            print(lines[i+2])
            break
    if not found:
      sys.exit("Id not found")      
  else:
    print("File not found")   

#  update user by id
def update_user():
    file_name = "user.txt"
    target_id  =  input("Which id you want to update: ").upper()
    New_first_name = input("Enter new first name: ")
    New_last_name = input("Enter new last name: ")
    found =False
    if os.path.exists(file_name):
      with open(file_name) as file:
        lines = file.readlines()
        for i in range(len(lines)):
          if lines[i].startswith("User id:"):
            user_id = lines[i].strip().split(":")[1]
            if target_id == user_id:
              found = True
              lines[i+1] = f"User Name:{New_first_name} {New_last_name}\n"
      if found:
        with open(file_name,"w") as file:
          file.writelines(lines)
          print("user updated successfully")
      else:
        print("User not found")
    else:
      print("file doesnot exists")

# update product by id
def update_product():
    file_name = "product.txt"
    target_id = input("Enter which id you want update: ").upper()
    new_product_name = input("Enter new product Name: ")
    new_product_price = input("Enter new Product price: ")
    found = False

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()

        for i in range(len(lines)):
            if lines[i].startswith("Product Id:"):
                product_id = lines[i].strip().split(":")[1]
                if target_id == product_id:
                    found = True
                    lines[i+1] = f"Product Name:{new_product_name}\n"
                    lines[i+2] = f"Product Price:{new_product_price}\n"
                    break 

        if found:
            with open(file_name, "w") as file:
                file.writelines(lines)
            print("Product updated!")
        else:
            print("Product not found")

    else:
        print("File not found!")
    
# delete user and product by id
def deleteuser():
   user_file = "user.txt"
   target_id = input("Enter Which id you want to deltete: ").upper()

   if os.path.exists(user_file):
      with open(user_file,"r") as file:
         lines = file.readlines()
      found =False
      for i, line in enumerate(lines):
         if line.strip().startswith(f"User id:{target_id}"):
            del lines[i:i+3]
            found = True
      if found:
         with open(user_file,"w") as file:
            file.writelines(lines)
            print("Record deleted")
      else:
         print("Id not found: ")

   else:
      print("File not found")     

def deleteproduct():
   product_file = "product.txt" 
   target_id  = input("Enter id which you want to delete: ").upper()
   
   if os.path.exists(product_file):
      with open(product_file,"r")as file:
         lines = file.readlines()
      found =False
      for i, line in enumerate(lines):
         if line.strip().startswith(f"Product Id:{target_id}"):
            del lines[i:i+4]
            found =True
      if found:
         with open (product_file,"w") as file:
            file.writelines(lines)
         print("record deleted")
      else:
         print("Id not found")
   else:
      print("File not found")
