class AutoMobile:
        # 접두어로 접근 속성 결정
        __name = "스마트"        # __ : Private, _ : Protected
        velocity = 0             # Public : _접두어가 없는 경우
        __Test__  = "apple"      # Public : __가 이름 양쪽으로 붙은 경우

        def TTTT(self):
            print("-----------")

        def velocityPlus(self):
            self.velocity=self.velocity + 1;
            self.TTTT()
            print('속도는 %d입니다.' %self.velocity)

        def velocityDw(self):
            self.velocity=self.velocity - 1;
            if self.velocity < 0:
                self.velocity = 0
            print('속도는 %d입니다.' %self.velocity)

ac=AutoMobile()
ac.velocityPlus()
ac.velocity=20
ac.velocityDw()
ac.__name = "임시값"
print(ac.__name)
#ac.TTTT()