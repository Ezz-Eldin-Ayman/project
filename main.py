from getpass import getpass
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(email):
    if re.fullmatch(regex, email):
        return True

    else:
        return False


data = {"acc": [], "pass": []}
product = {"name": [], "price": [], "quantity": []}
cart = []
q = []
price = []
total = []


def home():
    print("Hello To Small Project Created  By Ezz Eldin ")
    print("********** Home  Page **********")
    ch = input("To Login Enter 1 To Registration Enter 2 : ")

    if ch == "2":
        registration()
    elif ch == "1":
        login()
    else:
        print("Error Try Again")
        home()


def registration():
    print("********** SignUP  Page **********")
    mail = input("Enter Your Email : ")
    if check(mail):
        if mail in data["acc"]:
            print("Error Mail Is Already Exists Try Login  ")
            home()
        else:
            password = getpass("Enter Your Password : ")
            data["acc"].append(mail)
            data["pass"].append(password)
            login()
    else:
        print("Invalid Email")
        registration()


def login():
    print("********** Login  Page **********")
    mail = input("Enter Your Email : ")
    if check(mail):
        if mail in data["acc"]:
            # print(data["acc"].index(mail))
            password = getpass("Enter Your Password : ")
            if password in data["pass"]:
                if data["acc"].index(mail) == data["pass"].index(password):
                    print("Login Successful")
                    cont()
                else:
                    print("Wrong Password ")
                    login()
            else:
                print("Wrong Password")
                login()
        else:
            print("Wrong Mail ")
            home()
    else:
        print("Invalid Email")
        login()


def show():
    for i in range(len(product["name"])):
        print("Name : ", product["name"][i], "Price : ", product["price"][i], "Quantity : ", product["quantity"][i])


def add():
    show()
    pName = input("Enter The Product Name : ")
    if pName in product["name"]:
        print("Error Product Is Already Exists . ")
        add()
    else:
        product["name"].append(pName)
        product["price"].append(int(input("Enter The Product Price : ")))
        product["quantity"].append(int(input("Enter The Product quantity : ")))
        print("The Product is Added ")
        cont()
    cont()


def remove():
    show()
    de = input("Enter Product Name To Remove : ")
    if de in product["name"]:
        isAll = int(input("Enter Number of quantity you want to remove : "))
        de_number = product["name"].index(de)
        if isAll <= product["quantity"][de_number]:
            product["quantity"][de_number] = product["quantity"][de_number] - isAll
            if product["quantity"][de_number] - isAll == 0:
                product["name"].pop(de_number)
                product["price"].pop(de_number)
                product["quantity"].pop(de_number)
                cont()
        else:
            print("Number You Want To Remove Is Bigger Than The Quantity , Try Again .")
            remove()
    else:
        print("Error There is no product named " + de + " .")
        remove()
    cont()


def edit():
    show()
    ed = input("Enter Product Name To Edit : ")
    if ed in product["name"]:
        ed_number = product["name"].index(ed)
        print("* To Edit Product Name Enter 1")
        print("* To Edit Product Price Enter 2")
        print("* To Edit Product Quantity Enter 3")
        print("* Back To Menu Enter 9 ")

        ch = input("Enter Your Choice :")
        if ch == '1':
            print("Old Product Name :", product["name"][ed_number])
            newName = input("Enter New Product Name : ")
            product["name"][ed_number] = newName
        elif ch == '2':
            print("Old Product Price :", product["price"][ed_number])
            newPrice = int(input("Enter New Product Price : "))
            product["price"][ed_number] = newPrice
        elif ch == '3':
            print("Old Product Quantity :", product["quantity"][ed_number])
            newQuantity = int(input("Enter New Product Quantity : "))
            product["quantity"][ed_number] = newQuantity
        elif ch == '9':
            cont()
        else:
            print("Error Try Again")
            edit()
    else:
        print("Error There is no product named " + ed + " .")
        remove()
    cont()


def sale():
    show()
    isSale = input("Enter Product To Sale  ")
    if isSale in product["name"]:
        qua = int(input("Enter Number of quantity you want to Sale  : "))
        de_number = product["name"].index(isSale)
        if qua <= product["quantity"][de_number]:
            product["quantity"][de_number] = product["quantity"][de_number] - qua
            cart.append(product["name"][de_number])
            q.append(qua)
            price.append(product["price"][de_number])
            total.append(qua*product["price"][de_number])
            ch = input("Do You Want To Add another product Y Or N  : ")
            if ch == 'Y' or ch == 'y':
                sale()
            elif ch == 'N' or ch == 'n':
                print("*************** Cart ***************")
                for i in range(len(cart)):
                    print("Product Name : ", cart[i])
                    print("Quantity : ", q[i])
                    print("Price : ", q[i], "*", price[i], " = ", q[i]*price[i])
                print("Total Price Is : ", sum(total))
                cont()

            else:
                print("Error Try Again ")
                sale()

        else:
            print("Number You Want To Sale Is Bigger Than The Quantity , Try Again .")
            sale()
    else:
        print("Error There is no product named " + isSale + " .")
        sale()
    cont()


def cont():
    show()
    print("* To Add  Product Enter  1 ")
    print("* To Delete  Product Enter  2 ")
    print("* To Edit  Product Enter  3 ")
    print("* To Sale  Product Enter  4 ")
    print("* To Logout Enter 9 ")
    ch = input("Enter Your Choose : ")
    if ch == '9':
        home()
    elif ch == '1':
        add()
    elif ch == '2':
        remove()
    elif ch == '3':
        edit()
    elif ch == '4':
        sale()
    else:
        print("Error Chosen Try Again ")
        cont()


home()
