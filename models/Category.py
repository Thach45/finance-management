from jar import Jar

class Category:
    purposeSpend = "Chi tiêu"
    purposeIncome = "Thu nhập"
    purposeTransferAcc = "Chuyển khoản"
    purposes = [purposeSpend,purposeIncome,purposeTransferAcc]
    jar1 = Jar("Chi tiêu cần thiết")
    jar2 = Jar("Tiết kiệm dài hạn")
    jar3 = Jar("Quỹ giáo dục")
    jar4 = Jar("Quỹ hưởng thụ")
    jar5 = Jar("Quỹ tự do tài chính")
    jar6 = Jar("Quỹ từ thiện")
    jars = [jar1,jar2,jar3,jar4,jar5,jar6]
    def __init__(self,name = '',moneyGoal=1000000,jar=jars[0],purpose = purposes[0]):
        self.__name = name
        self.__money = 0
        if moneyGoal < 0:
            self.moneyGoal = 0
        else:
            self.__moneyGoal = moneyGoal
        self.__jar = jar
        self.__purpose = purpose

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,value):
        if value >= 0:
            self.__money = value
        else: 
            return False
    
    @property
    def moneyGoal(self):
        return self.__moneyGoal
    
    def SetMoneyGoal(self,value):
        if value>0:
            self.__moneyGoal = value
        else: 
            return False
        
    @property
    def jar(self):
        return self.__jar.name
    
    @property
    def purpose(self):
        return self.__purpose
    
    
# def transaction(category:Category,value):
#     category.money = category.money + value
#     category.jar.money = category.jar.money + value

# anuong = Category("anuong",jar1)
# dichuyen = Category("dichuyen",jar1)

# transaction(anuong,100)
# transaction(dichuyen,200)

# print(anuong.money)
# print(dichuyen.money)
# print(jar1.money)