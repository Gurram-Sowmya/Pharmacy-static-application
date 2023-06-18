import csv
def collect():
    d = [sign_up()]
    fp = open(r'login_system_1.csv', 'a', newline="")
    res = csv.DictWriter(fp, ['ID', 'USERNAME', 'PASSWORD','CART'])
    if fp.tell() == 0:
        res.writeheader()
    res.writerows(d)
    fp.close()
    home_content()

def sign_up():
    name = input("Enter your username: ")
    password = input("Enter your password: ")
    def special_char():
        l=['!', '#', '@', '$', '%', '&']
        for i in password:
            if i in l:
                return True
        return False

    def num_char():
        l1=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in password:
            if i in l1:
                return True
        return False

    def small_alpha_char():
        l2=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in password:
            if i in l2:
                return True
        return False
    def password_enter():
        nonlocal password
        password = input("Re-enter your password: ")
        return check()   

    def check():
        if password[0].isupper() and special_char() and num_char() and small_alpha_char():
            return password
        else:
            print("NOTE: PASSWORD SHOULD START WITH AN UPPERCASE CHARACTER, CONTAIN ONE SPECIAL CHARACTER ['!', '#', '@', '$', '%', '&'], ONE NUMERIC CHARACTER, AND ONE LOWERCASE CHARACTER")
            return password_enter()
    
    def read_csv():
        fp = open(r'G:\py_project\login_system_1.csv', 'r', newline='')
        reading = csv.DictReader(fp)
        l=[]
        for i in reading:
            l+=i['ID']
        return len(l)
    l1=read_csv()
    l2=l1+1

    password = check()
    return {'ID':l2,'USERNAME': name, 'PASSWORD': password}

def check_account():
    output = input("Do you have an account? (YES/NO): ")
    if output.upper() == 'NO':
        print("Please sign up to create an account")
        collect()
        print('Thank you for signing up! Your account has been created.')
    else:
        print("Please enter your username and password")
        name = input("Enter your username: ")
        pas = input('Enter your password: ')
        with open(r'login_system_1.csv', 'r') as fp:
            res = csv.DictReader(fp, ['ID', 'USERNAME', 'PASSWORD','CART'])
            L = []
            d = []
            for i in res:
                L.append(i['USERNAME'].upper())
                d.append(i)
            for i in d:
                if name.upper() in L:
                    if name.upper() == i['USERNAME'].upper() and pas == i['PASSWORD']:
                        home_content()
                        break
                    elif name.upper() == i['USERNAME'].upper() and pas != i['PASSWORD']:
                        print("Password is incorrect")
                        break
                else:
                    if name.upper() != i['USERNAME'].upper() and pas != i['PASSWORD']:
                        print("Username and password are incorrect")
                        break
                    elif name.upper() != i['USERNAME'].upper():
                        print("Username is incorrect")
                        break


def home_content():
    print('*' * 120)
    i = 0
    while i < 5:
        if i == 1:
            print("Welcome to Pharmacy".center(120))
        elif i == 3:
            print("All kinds of pharmacy products available here.".center(120))
        elif i == 4:
            print('*' * 120)
            print("1) PRODUCTS     2) SEARCH     3) DESCRIPTION     4) CART     5) PAYMENT     6) LOGIN     7)HELP     8)EXIT".center(120))
            print('*' * 120)
        print()
        i += 1
    home_menu()


def home_menu():
    products = {
        "prescription": ["acetaminophen", "ibuprofen", "amoxicillin","ACE inhibitors","beta blockers","diuretics","acetaminophen","Naprosyn","Ketrolac"],
        "OTC medicines": ["aspirin", "antacids", "cough and cold medications"],
        "supplies and equipment": ["bandages", "blood pressure monitors", "inhalers"],
        "vitamins and supplements": ["multivitamins", "fish oil supplements", "probiotics"],
        "personal care": ["shampoo", "toothpaste", "soap"]
    }
    cart=[]
    def payment():
        print('PAYMENT')
        if len(cart)==0:
            print("your cart is empty")
            return
        if len(cart)!=0:
            total =0
            for item in cart:
                total += 100
            print(f'Total cost: ₹{total}')
            payment_method = input('Enter payment method (credit card(Enter "1")/paytm (Enter "2"): ')
            if int(payment_method)== 1:
                card_number = input('Enter credit card number: ')
                cvv = input('Enter CVV: ')
                print('Payment successful!')
                print(cart,'of price',total,'is getting delivered')
                fp = open(r'login_system_1.csv', 'a', newline="")
                res = csv.DictWriter(fp, ['ID', 'USERNAME', 'PASSWORD','CART'])
                data={'CART':cart}
                res.writerows(data)
                fp.close()
            elif int(payment_method.lower())==2:
                email = input('Enter Paytm email: ')
                password = input('Enter Paytm password: ')
                print('Payment successful!')
                print(cart,'of price ₹',total,'is getting delivered')
                fp = open(r'login_system_1.csv', 'a', newline="")
                res = csv.DictWriter(fp, ['ID', 'USERNAME', 'PASSWORD','CART'])
                res.writerows({'CART':cart})
                fp.close()
            else:
                print('Invalid payment method.')





    def add_cart():
        add_to_cart= list(input("Enter the number of the medicine you want to add to your cart: "))
        l=[]
        for i in add_to_cart:
            l+=[int(i)]
            for i in l:
                n=i-1
            cart.append(products[b][n])
        print("***********************The medicines are added to cart********************")

    def medicines_list():
        count=1
        for medicine in products[b]:
            print(f"{count}){medicine}",end=" ")
            count+=1
        print()
    while True:
        n = int(input('Choose an option: '))
        if n == 1:
            print('PRODUCTS AND SERVICES:')
            print("1) Prescription   2) OTC medicines   3) Supplies and Equipment   4) Vitamins and Supplements   5) Personal care 6)Exit".center(120))
            while True:
                z=int(input("Enter the service you want:"))
                
                if z==1:
                    a=z-1
                    b=list(products)[a]
                    medicines_list()
                    add_cart()
                elif z==2:
                    a=z-1
                    b=list(products)[a]
                    medicines_list()
                    add_cart()
                elif z==3:
                    a=z-1
                    b=list(products)[a]
                    medicines_list()
                    add_cart()
                elif z==4:
                    a=z-1
                    b=list(products)[a]
                    medicines_list()
                    add_cart()
                elif z==5:
                    a=z-1
                    b=list(products)[a]
                    medicines_list()
                    add_cart()
                elif z==6:
                    break
        elif n == 2:
            print('SEARCH')
            s=input('enter the medicine you want: ')
            found = False
            for category, items in products.items():
                if s in items:
                    print(f"{s} found in {category}")
                    found = True
            if not found:
                print(f"{s} not found in any category")
        elif n == 3:
            print('DESCRIPTION')
            s=eval(input('enter the medicine name: '))
            for category, items in products.items():
                if s in items:
                    print(f"Description of {s}:")
                    if s == "acetaminophen":
                        print("Acetaminophen (APAP - Also known as paracetmol in many countries) is an non-opiod analgesic and antipyretc agent used to treat pain fever.")
                    if s== "ibuprofen":
                        print("Nonprescription ibuprofen is used to reduce fever and to relieve minor aches and pain from headaches, muscle aches, arthritis, menstrual periods, the common cold, toothaches, and backaches.")
                    if s== "amoxicillin":
                        print("It is used to treat bacterial infections, such as chest infections (including pneumonia) and dental abscesses. It can also be used together with other antibiotics and medicines to treat stomach ulcers.")
                    if s== "ACEinhibitors": 
                        print("ACE inhibitors are a medication class used to treat and manage hypertension, a significant risk factor for coronary disease, heart failure, stroke, and a number of other cardiovascular conditions. Most cases are primary and not attributable to any specific etiology.")
                    if s== "betablockers":
                        print("Beta blockers may be used to treat: angina – chest pain caused by narrowing of the arteries supplying the heart. heart failure – failure of the heart to pump enough blood around the body. atrial fibrillation – irregular heartbeat.")
                    if s== "diuretics":
                        print("Diuretics, also called water pills, are a common treatment for high blood pressure. Find out how they work and when you might need them. Diuretics, sometimes called water pills, help rid your body of salt (sodium) and water. Most of these medicines help your kidneys release more sodium into your urine.")
                    if s== "acetaminophen":
                        print("Nonprescription naproxen is used to reduce fever and to relieve mild pain from headaches, muscle aches, arthritis, menstrual periods, the common cold, toothaches, and backaches. Naproxen is in a class of medications called NSAIDs.")
                    break
            else:
                print(f"{s} not found in any category")
        elif n == 4:
            if len(cart)==0:
                print("your cart is empty")
            else:
                print('your orders are here')
                print('************CART**************\n',cart)
                print("1) To remove items from the cart \n2) proceed to buy the items in cart")
                choose_user=int(input("choose an option from above"))
                if choose_user==2:
                    payment()
            
        elif n == 5:
            def payment():
                print('PAYMENT')
                if len(cart)==0:
                    print("your cart is empty")
                    return
                if len(cart)!=0:
                    total =0
                    for item in cart:
                        total += 100
                    print(f'Total cost: ₹{total}')
                    payment_method = input('Enter payment method (credit card(Enter "1")/paytm (Enter "2"): ')
                    if int(payment_method)== 1:
                        card_number = input('Enter credit card number: ')
                        cvv = input('Enter CVV: ')
                        print('Payment successful!')
                        print(cart,'of price',total,'is getting delivered')
                    elif int(payment_method.lower())==2:
                        email = input('Enter Paytm email: ')
                        password = input('Enter Paytm password: ')
                        print('Payment successful!')
                        print(cart,'of price ₹',total,'is getting delivered')
                    else:
                        print('Invalid payment method.')
            payment()
            home_menu()
        elif n==6:
            check_account()
            
        else:
            print('need any help contact :9638520741')
            print("Thank you")
            print('visit again')
            exit()
home_content()