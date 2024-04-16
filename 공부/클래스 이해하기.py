# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:40:16 2024

@author: moon
"""
# __init__ : 생성자 함수
class Monster:
    def __init__(self,name): # self 객체 자기 자신 name은 속성값
        self.name = name
    def x(self): # shark
        print(f"나는{self.name}")
shark = Monster("상어") # 몬스터 클래스로부터 객체를 만들어내는데 매개변수로 상어를 넣어줌
print(shark.name)
wolf=Monster("늑대")
wolf.x()
