class New_Members:

    def __init__(self,name,age,email,mobile):
        self.__name=name
        self.__age=age
        self.__email=email
        self.__mobile=mobile
             
    def setName(self,name):
        self.__name=name

    def setAge(self,age):
        self.__age=age

    def setEmail(self,email):
        self.__email=email

    def setMobile(self,mobile):
        self.__mobile=mobile       

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getEmail(self):
        return self.__email

    def getMobile(self):
        return self.__mobile

    def details(self):
        return f"{self.__name}/{self.__age}/{self.__email}/{self.__mobile}/\n"