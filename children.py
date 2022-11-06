#Author - Jayspay
#Word - Children
#Team - Dillusioners
#Info - Children's toy shop

import os
import json
#Initial Display
print("###################################################################")
print("                     Welcome to the toy store                      ")
print("###################################################################")
#Menu Display
def toy_display():
    print("Toys for boys(11-14):- \n1.Racing Car - 100$\n2.RC Drone - 500$\n3.Stretch Armstrong-20$")
    print("Toys for boys(6-10):- \n4.Fake light saber - 60$\n5.Omnitrix - 80$\6.Bugatti - 120$")
    print("Toys for boys(0-5):- \n7.Sound Bells - 5$\n8.Beyblade - 40$\n9.Ching Cheng Hanji - 1000$")
    print("Toys for girls(11-14):- \n10.Annabella - 100$\n11.Barbie Human - 500$\n12.Bat-20$")
    print("Toys for girls(6-10):- \n13.Scarlett Witch Hologram - 60$\n14.Omnitrix Girl Edition- 80$\15.Mercedes- 120$")
    print("Toys for girls(0-5):- \n16.Sound Bells - 5$\n17.Art Pencils Rubber imitations - 40$\n18.Toy phone - 1000$")
    print("** Even though toys are gendered marked you can buy any of them as per your choice")

#Price calculator function
def price(lst,price_dict):
    amount = 0
    for i in range(len(lst)):
        amount += price_dict[lst[i]]
    return amount
#Transaction recorder function
def transaction_append(pur):
    try:
        name = input("Please enter you name")
        age = int(input("Please enter age"))
        sus_code = input("Please enter your sus code ;)")
        if(age < 18):
            print("You cannot purchase here kid call your parents")
    except Exception as e:
        print("OOPS :(")
    else:
        data = {
                "name":name,
                "age":age,
                "sus_code":sus_code,
                "purchase":pur
                }

        filename = "Fare/" + sus_code + ".json"
        print("Your transaction ID is: " + sus_code + "\n")
        jsonObj = json.dumps(data)
        with open(filename, "w") as f:
            f.write(jsonObj)


#Main function to call other functions
def main():
    toy_display()
    toy_price = {1:100,2:500,3:20,4:60,5:80,6:120,7:5,8:40,9:1000,10:100,11:500,12:20,13:60,14:80,15:120,16:5,17:40,18:1000}
    toy_num_arr = []
    while(True):
        try:
            choice = int(input("Enter the choice you want or 0 to exit : "))
            if choice in toy_price:
                toy_num_arr.append(choice)
                print("Ok choose another toy if you want")
            elif choice == 0:
                print("Ok")
                break
            else:
                print("Toy is non existant")
        
        except Exception as e:
            print("Something went wrong :(",e)
    
    Cost = price(toy_num_arr,toy_price)
    print("Your total price will be ",Cost)
    transaction_append(Cost)
#Execute function to create directories and run main()
def execute():
    try:
        if not os.path.exists('ids'):
            os.makedirs('ids')
            if not os.path.exists('Fare'):
                os.makedirs('Fare')
                main()
        else:
            main()
    except Exception as e:
        print("Error: " + str(e))
#Calling execute()
execute()