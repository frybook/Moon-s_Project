class Student:

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

        self.my_sum = self.kor+self.eng+self.math
        self.my_avg = self.my_sum/3.0

        print("%4s\t%3d\t%5d\t%3d\t%5d\t%5.2f" % 
              (self.name, self.kor, self.eng, self.math, 
               self.my_sum, self.my_avg))



print("="*40)
print("  학생  국어  영어  수학  합   평균")
print("="*40)
#         name    kor eng math  순으로 적어넣음 
Student("김길동", 87, 98, 88)
Student("연우연", 92, 98, 96)
Student("구지연", 76, 96, 94)
Student("김소라", 98, 92, 96)
Student("이지연", 95, 98, 98)
Student("윤지우", 64, 88, 92)
#%%
a = Student("김길동", 87, 98, 88)
b = Student("연우연", 92, 98, 96)
c = Student("구지연", 76, 96, 94)
d = Student("김소라", 98, 92, 96)
f = Student("이지연", 95, 98, 98)
g = Student("윤지우", 64, 88, 92)
print(a.name)
print(b.name)

#%%

a = 'ABC'
b = 90
print(" 1234567890" * 2)
print("[%6s\t%3d]" % (a,b)) 
