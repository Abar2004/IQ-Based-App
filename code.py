from Question import Question
import time
import random

class main_menu:
    point = 0
    iq = 0
    def  add(self,q,p):
        self.iq =self.iq + q
        self.point =self.point + p
        return self.iq , self.point
    def profile(self,user,name):
        self.user =  user
        self.name = name
        print("Thanks for Registration ! We welcome you {} ".format(self.name))
        return self.name
    def show(self):
        print("Your IQ is ",self.iq)
        print("And Yours point ",self.point)
m=main_menu()
class daily_task(main_menu):
    def sel(self,name):
        print("{} ! your IQ level is {} ",format(self.name,self.iq))


d=daily_task()
question_prompt = ["Question",
                   "1. A biconvex lens has radii ofcurvature,20cm each.If the refraction index of the matrix of the lens 1.5,the power of the lens is \n(a)+5D\n(b)infinity\n(c)+2D\n\n",
                    "2. Two abject of mass 10 kg and 20 kg respectievly are connected to the ends of a rigid rod of lenght 10m with negligible mass.the distence of the center of the mass of the system from the 10kg mass is \n(a)10m\n(b)5m\n(c)20/3m",
                    "3. The ratio of the distence travelled by a frelly falling body in the 1st,2nd,3rd and 4th second\n(a)1:3:5:7\n(b)1:1:1:1\n(c)1:2:3:4\n\n",
                    "4. The theory of relativity is presented by which scientist\n(a)Albert einstein\n(b)issac newton\n(c)Marie curie \n\n",
                    "5. what type of lens is used in a magnifing glass \n(a)concave\n(b)convex\n(c)none of the above \n\n",
                   #Biology
                   "1. Ordinary table salt is sodium chloride .What is baking soda ?\n(a)potassium chloride\n(b)potassium carbonate\n(c)sodium bicarbonate\n\n ",
                   "2. ozone hole refers to \n(a)hole in ozone layer\n(b)decrease in the ozone layer in troposphere\n(c)decrease in thickness of ozone layer in stratosphere\n\n",
                   "3.polination is best difined as \n(a)transfer of pollen from anther to stigma\n(b)germination of pollen grains\n(c)growth of pollen tube in ovuel\n\n",
                   "4. plants receive their nutrients mainly from \n(a)atmosphere\n(b)light\n(c)soil\n\n",
                   "5.movement of cell against concentration gradient is called \n(a)Osmosis\n(b)active transport\n(c)diffusion\n\n",
                   #GK
                   "1. grant center terminal,park avenue,new york is the worlds\n(a)largest railway station\n(b)highest railway station\n(c)none of the above\n\n",
                   "2. Entomology is the science  that studies \n(a)behavior of human beings\n(b)insects\n(c)the formation of rocks\n\n",
                   "3. Eritrea,which became the 182nd membor of UN in 1993,is in the continent of \n(a)asia\n(b)africa\n(c)Europe",
                   "4. Garampani  santuary is located at \n(a)junagar,gujarat\n(b)dihun,assam\n(c)gangtok,sikkim\n\n",
                   "5. Hitler party which came into power in 1993 is known as\n(a)labour paerty\n(b)nazi party\n(c)democratic party\n\n"]
#Physics_Question
question = [
    Question(question_prompt[1],'a'),
    Question(question_prompt[2],'c'),
    Question(question_prompt[3],'a'),
    Question(question_prompt[4],'a'),
    Question(question_prompt[5],'b')
    ]
def run_test1(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        answer = input("Answer : ")
        if answer==question.answer:
            score=score+1
    q=score/100
    p=score/100+0.01
    m.add(q,p)
    time.sleep(5)
    print("We calculated your IQ by you answer the above questions \nAnd by this calculation you got ")
    m.show()
    time.sleep(5)
    print("This is only temporary IQ \n It may change According you answeres correctly ")
#Biology_Question
question2 = [
    Question(question_prompt[6],'c'),
    Question(question_prompt[7],'c'),
    Question(question_prompt[8],'a'),
    Question(question_prompt[9],'c'),
    Question(question_prompt[10],'b')
    ]
def run_test2(questions):
    score = 0
    for question2 in questions:
        print()
        answer = input(question.prompt)
        if answer==question.answer:
            score=score+1
    q=score/100
    p=score/100+0.01
    m.add(q,p)
    m.show()
#Gk_Question
question3 = [
    Question(question_prompt[11],'a'),
    Question(question_prompt[12],'b'),
    Question(question_prompt[13],'b'),
    Question(question_prompt[14],'b'),
    Question(question_prompt[15],'b')
    ]
def run_test3(questions):
    score = 0
    for question3 in questions:
        print(question.prompt)
        answer = input("Answer : ")
        if answer==question.answer:
            score=score+1
    q=score/100
    p=score/100+0.01
    m.add(q,p)
    m.show()
'''
def otp():
    a=[1,2,3,4,5,6,7,8,9,0]
    x=random.random()
    '''
def login():
    na=input("Your's Name : ")
    number=input("Enter your Mobile Number .... ")
    print("We have sent one time password to your  Mobile Number ")
    time.sleep(6)
    us=input("Enter OTP: ")
    if us!='88700':
        print("\aIncorrect OTP\nTRY AGAIN\a")
        time.sleep(2)
        welcome()
    



def welcome():
    time.sleep(5)
    print("Hi ! User we came to test your IQ and make to improve your IQ more and more")
    time.sleep(5)
    print("Let's register first ")
    login()
    m.profile(us,na)
    time.sleep(10)
    print("Let's  start ")
    print("You have to answer some questions to know your IQ level to us it is usefull to fetching questions and to improve your IQ-Level")
    time.sleep(5)
    print("We fetching some question for you .......")
    time.sleep(5)
    run_test1(question)
    time.sleep(5)
    print("This is the chance to increase your IQ\nSome questions are preparing for you ",na)
    c=input("Do you want to continue press(1) or Home press(2) : ")
    if c!=1:
        print("")
    else:
        run_test2(question)
        d.sel(na)        
        run_test3()

print("\t\t\tTHIS IS IQ BASED APP \n")
while True:
    print("1.LOGIN\n2.CREATE\n3.HOME\n2.IQ-TEST\n3.PROFILE\n4.EXIT")
    ans=int(input("your answer..... "))
    if ans==1:
        print("\t\t\tLOGIN")
        welcome()
        break

