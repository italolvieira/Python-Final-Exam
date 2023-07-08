import NMembers
import VideoInput
#-------------------------------------------------------------------------------
def main():
    x = int(input("How many New Members do you want to add?: "))
    #NEW MEMBERS SCREEN
    print("_____________________________________________________________________")
    print("|NEW MEMBERS|")
    newmembers={}
 
    for mem in range(x):
        name=str(input("\nName: "))
        age=int(input("Age: "))
        email=input("Email: ")
        mobile=int(input("Phone Number: "))
        print("-------------------------------")
        allmembers=NMembers.New_Members(name,age,email,mobile)
        newmembers[mem]=allmembers   
        NewMembers=open("StoreMembers.txt","w")

    for key in range(x):
        NewMembers.write(str(newmembers[key].details()))
#-------------------------------------------------------------------------------
    #VIDEO INPUT SCREEN    
    print("_____________________________________________________________________")
    print("\n|RENT INFORMATION|")
    stop=2
    rentinfo={}

    for rent in range(x):
        memberID=input("\nMemberID: ")
        customer=str(input("Name: "))
        title=input("Title: ")
        type=(input("Type: "))
        date=input("Date: ")
        rentals=int(input("Rent cost: "))
        paid=int(input("Paid: "))
        print("-------------------------------")
        lcharges=rentals-paid
        allinfo=VideoInput.Video_Input(customer,title,type,date,rentals,paid,memberID,lcharges,name,age,email,mobile)
        rentinfo[rent]=allinfo
#-------------------------------------------------------------------------------
    print("_____________________________________________________________________")
    print("\nSUMMARY REPORT")
    print("\nCUSTOMERS   RENTALS    LATE CHARGES    TITLE")
    for key in range(x): 
        print(rentinfo[key].details())                      
#-------------------------------------------------------------------------------    
if __name__=="__main__":
   main() 
