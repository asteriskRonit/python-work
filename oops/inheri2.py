class student:
    #public
    name=None
    #protected
    _age=None
    #private
    __rollno=None
    
    def insert_data(get,name,age,roll):
        get.name=name
        get._age=age
        get.__rollno=roll
    def print_value(self):
        print("Name=",self.name," age",self._age," roll no = ",self.__rollno)   

object1=student()
object1.insert_data("rahul",20,"op001")   
object1.print_value()  
print("from outside ",object1.name,object1._age)  