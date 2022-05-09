class student():
    institution='IIPS'
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print("--------------------------")
        print("Marks in python=",self.a)
        print("Marks in DBMS=",self.b)
        print("--------------------------")
    @classmethod
    def info(self):
        print("Class belong to",self.institution)

    @staticmethod
    def about():
        print("This class hold the data of marks obtain by studdent  in python and DBMS in IIPS")
s1=student(17,18)
s2=student(15,15)
s3=student(16,13)
s1.show()
s2.show()
s3.show()
student.info()
student.about()


