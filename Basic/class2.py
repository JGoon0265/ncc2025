class Student():
    def __init__(self,name,age,like):
        self.name=name
        self.age=age
        self.like=like
    def studentinfo(self):
        print(f"이름:{self.name}, 나이:{self.age}, 좋아하는 것:{self.like}")
        
a1=Student("정지용",26,"드라이브")
a2=Student("조하선",22,"ott보기기")
a1.studentinfo()
a2.studentinfo()