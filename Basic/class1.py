class Mother():
    def characteristic(self):
        print("빨간머리이다.")
        print("검정신발을신고있다.")
class Daughter(Mother):
    def characteristic(self):
        super().characteristic()
        print("노란머리이다.")
        
mom = Mother()
d = Daughter()
print("엄마는")
mom.characteristic()
print("딸은")
d.characteristic()