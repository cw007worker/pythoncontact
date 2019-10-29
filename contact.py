class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
    def print_info(self):
        print("Name:", self.name)
        print("Phone Number:", self.phone_number)
        print("Email:", self.e_mail)
        print("Address:", self.addr)
        print("=====================")

def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("Email: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name+'\n')
        f.write(contact.phone_number+'\n')
        f.write(contact.e_mail+'\n')
        f.write(contact.addr+'\n')
    f.close()

def load_contact(contact_list):
    f = open("contact_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4*i].rstrip('\n')
        phone = lines[4*i+1].rstrip('\n')
        email = lines[4*i+2].rstrip('\n')
        addr = lines[4*i+3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()
def print_menu():
    print("1. enter the contract")
    print("2. output the contract")
    print("3. delete the contract")
    print("4. exit")
    menu = input("select the menu: ")
    return int(menu)
def main():

    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        if menu == 2:
            print_contact(contact_list)
        if menu == 3:
            name = input("Name: ")
            delete_contact(contact_list, name)
        if menu == 4:
            store_contact(contact_list)
            break
if __name__ == "__main__":
    main()



