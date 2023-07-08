
import os
import csv
import datetime
from time import strftime

def title():

  TE = "Contacts Book"
  print(TE)

class contact_numbers:
   contact_fields = ["Name", "Mobile_No"]
   contact_database = "contacts.csv"
   contact_data = []
   
   def create(self):
    os.system('cls')
    title()
    print("    Create Contact:")
    for fields in self.contact_fields:
      contact_details = input(" Enter " + fields + ":")
      self.contact_data.append(contact_details)
      
    Date = datetime.datetime.today()
    d = Date.strftime("%B %d %Y")
    self.contact_data.append(d)

    with open(self.contact_database, 'a') as file:
      write = csv.writer(file)
      write.writerows([self.contact_data])
    self.contact_data=[]
    print("Contact is created successfully")

    
    print("\n")   
   def view(self):
      os.system('cls')
      title()
      print("Contacts:")
      count = 0
      with open(self.contact_database, 'r') as file:
       read = csv.reader(file)
       for data1 in read:
         if len(data1) > 0:
            count = count + 1
       print("Total Contacts: ", count)
       print("")

      with open(self.contact_database, 'r') as file:
       read = csv.reader(file)
       if os.path.getsize(self.contact_database)==0: print("Contact Book is empty, Please create contacts")
       else:
         for fields in self.contact_fields:
            print(format(fields), end="\n")
            print(format("Date"))
        #  print(format('----','---------','----')) 
         for data in read:      
            for item in data:
                 print( format(item), end="\t\t")  
      input("\t Press enter key to continue..")
      os.system('cls')
   def search(self):
      os.system('cls')
      title()
      print("Search Contacts:")
      self.contact_person_match = 'false'
      search_value = input("Enter your name: ")
      for fields in self.contact_fields:
         print(format(fields), end="")
      print(format("Date"))
      print('----','---------','----')
      print("")
      with open(self.contact_database, 'r') as file:
         read = csv.reader(file)
         for data in read:
          if len(data)>0:
           if search_value == data[0]:
            self.contact_person_match = 'true'
            print( '{:<10}\t\t{:<10}\t\t{:<10}'.format(data[0], data[1], data[2]))
      if self.contact_person_match == 'false':
         print("")
         print("Sorry!, there is no contact by this name")  
      print("")

       

   def delete(self):
        os.system('cls')
        title()
        print("")
        print("Delete Contacts:")
        print("----------------")
        print("")
        
        self.contact_person_match = 'false'
        update_contact = input("Enter the name: ")
        update_list = []
        with open(self.contact_database, 'r') as file:
         read = csv.reader(file)
         for data in read:
          if len(data)>0:
           if update_contact != data[0]: 
              update_list.append(data)
           else:
              self.contact_person_match = 'true'
   
         if self.contact_person_match == 'true':
            with open(self.contact_database, 'w') as file:
              write = csv.writer(file)
              write.writerows(update_list)
              print("")
              print("Contact is deleted successfully!")
              print("")
        if self.contact_person_match == 'false':
            print("")
            print("Sorry! data not found")
            print("")
contact_class = contact_numbers()
os.system('cls')
title()
while True:
  print("1. Show Contacts list")
  print("2. Create Contact")
  print("3. Search Contacts")
  print("4. Delete Contacts")
  print("5. Exit")
  option = int(input("Choose you option: "))
  if option == 1: 
   contact_class.view()
   title()

  if option == 2:
   while True:
    contact_class.create()
    ans = input("create another contact detail (yes/no): ")
    if ans == 'yes' or ans == 'Yes':
      continue
    else:
       break
   os.system('cls')
   title()

  if option == 3:
   while True:
    contact_class.search()
    print("")
    ans = input("search contact number(yes/no): ")
    if ans == 'Yes' or ans == 'yes':
      continue
    else:
       break
   os.system('cls')
   title()

  if option == 4:
   while True:
      contact_class.delete()
      ans = input("delete contact detail(yes/no): ")
      if ans == 'Yes' or ans == 'yes':
        continue
      else: break
   os.system('cls')
   title()

  if option == 5:
   os.system('cls')
   Tq= "Thank you for using this software"
   print("\n")
   print(Tq)
   break

  if option > 5 or option < 1:
      os.system('cls')
      print("Invalid choice. Please choose valid option")
      print("\n")
      input("Press enter key to continue...")
      os.system('cls')
      title()

  