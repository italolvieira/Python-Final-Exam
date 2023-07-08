import NMembers

class Video_Input:

    def __init__(self,customer,title,type,date,rentals,paid,memberID,lcharges,name,age,email,mobile):
        self.__title=title
        self.__type=type
        self.__date=date
        self.__memberid=memberID
        self.__rentals=rentals
        self.__paid=paid
        self.__customer=customer
        self.__lcharges=lcharges
       
    def setTitle(self,title):
        self.__title=title

    def setType(self,type):
        self.__type=type

    def setDate(self,date):
        self.__date=date

    def setMemberID(self,memberID):
        self.__memberid=memberID

    def setRentals(self,rentals):
        self.__rentals=rentals

    def setPaid(self,paid):
        self.__paid=paid

    def setCustomer(self,customer):
        self.__customer=customer

    def setLcharges(self,lcharges):
        self.__lcharges=lcharges     

    def getTitle(self):
        return self.__title

    def getType(self):
        return self.__type

    def getDate(self):
        return self.__date    

    def getMemberID(self):
        return self.__memberid

    def getRentals(self):
        return self.__rentals    

    def getPaid(self):
        return self.__paid

    def getCustomer(self):
        return self.__customer

    def getLcharges(self):
        return self.__lcharges

    def details(self):
        return f"{self.__customer}     {self.__rentals}$     {self.__lcharges}$     {self.__title}"