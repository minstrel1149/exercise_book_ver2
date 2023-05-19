
#Chapter 2

# 한글 입력
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font',family =font_name)

######################### 3.1  #########################
#input data
data = {'단과대학' : ["공과대", "자연대", "경영대", "사범대", "법대", "사회대", "가정대"],
        '학생수'   : [1300, 300, 500, 300, 200 , 400, 170],
        '학과수'   : [20, 6, 5, 6, 3, 8, 3]}

# pie chart
import matplotlib.pyplot as plt
plt.figure()
plt.pie(data["학생수"],labels=data["단과대학"],autopct='%1.1f%%')
plt.title("안전사고에 대한 연구")
plt.show()
plt.savefig('./plot/연습문제1.png')
# bar chart
import numpy as np
rf = data['학생수'] / np.sum(data['학생수'])
plt.figure()
plt.bar(data['단과대학'], rf)
plt.title("단과대별 학생수")
plt.xlabel("단과대학")
plt.ylabel("상대도수")
plt.show()
plt.savefig('./plot/연습문제2.png')
######################### 3.2  #########################
#input data

accident = {'구분' : ['추락사고', '화상', '열사병', '타박상', '부주의', '기타', '합계'],
            '도수' : [329, 256, 219, 202, 40, 86, 1132]}

#pie chart
import matplotlib.pyplot as plt
plt.figure()
plt.pie(accident["도수"][0:6],labels=accident["구분"][0:6],autopct='%1.0f%%')
plt.title("안전사고에 대한 연구")
plt.show()
plt.savefig('./plot/연습문제3.png')
#  accident_rf = accident['도수'] / np.sum(accident['도수'])

# bar plot
plt.figure()
plt.bar(accident['구분'], accident['도수'])
plt.title("안전사고에 대한 연구")
plt.xlabel("구분")
plt.ylabel("도수")
plt.show()
plt.savefig('./plot/연습문제4.png')


######################### 3.3  #########################
#input data
money = {'구분' : ['개인과자선단체','사업','재단','합계'],
         '모금액': [11700,2400,6600,20700]}

#pie plot
import matplotlib.pyplot as plt
plt.figure()
plt.pie(money["모금액"][0:3],labels=money["구분"][0:3],autopct='%1.0f%%')
plt.title("대학기금모금운동")
plt.show()
plt.savefig('./plot/연습문제5.png')
#bar plot
import matplotlib.pyplot as plt
plt.figure()
plt.bar( money['구분'][0:3], money['모금액'][0:3])
plt.title("대학기금모금운동")
plt.ylabel("모금액")
plt.show()
plt.savefig('./plot/연습문제6.png')

######################### 3.4  #########################
#input data
commute = {'통근수단' : ['나홀로자가용','승용차함께타기','대중교통','기타'],
           '도수' : [8500,1000,400,100]}

#pie plot
import matplotlib.pyplot as plt
plt.figure()
plt.pie(commute["도수"],labels=commute["통근수단"],autopct='%1.0f%%')
plt.title("교통문제에 관한 조사")
plt.show(block=True)
plt.savefig('./plot/연습문제7.png')
#bar plot

import matplotlib.pyplot as plt
plt.figure()
plt.bar(commute['통근수단'],commute['도수'])
plt.title("교통문제에 관한 조사")
plt.ylabel("도수")
plt.xlabel("통근수단")
plt.show()
plt.savefig('./plot/연습문제8.png')

######################### 3.5  #########################
from paretochart import pareto
import matplotlib.pyplot as plt
deficit = {"결합의 종류" : ["차체","보조장비","전기","전동장치","엔진"],
           "발생건수" : [72,53,12,8,5]}
plt.figure()
pareto(deficit['발생건수'],line_args={'red',},labels=deficit['결합의 종류'])
plt.show(block=True)
plt.savefig("연습문제3.5.png" )

######################### 4.1  #########################
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
computer = np.array([1,3,1,1,0,1,0,1,1,0,
                     2,2,0,0,0,1,2,1,2,0,
                     0,1,6,4,3,3,1,2,4,0])
#table
computer_t = pd.crosstab(index = computer , columns= '도수')
print(computer_t)
#pie
computer_t.plot(kind='pie',autopct='%1.0f%%',subplots=True,legend=False)
plt.title("컴퓨터 작동 정지 횟수")
plt.ylabel("")
plt.show(block=True)
plt.savefig("연습문제4.1.2.png")
#bar
computer_t.plot(kind='bar',legend=False)
plt.title("컴퓨터 작동 정지 횟수")
plt.xlabel("")
plt.show(block=True)
plt.savefig("연습문제4.1.3.png")

######################### 4.2  #########################
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

baby = np.array([1,5,2,1,3,4,2,2,1,1,
                 3,2,3,1,4,1,1,2,5,1,
                 2,2,2,1,2,3,2,2,2,2,
                 2,2,3,3,2,1,2,2,2,1,
                 1,3,1,3,3,2,1,1,2,2])
#table
baby_t = pd.crosstab(index=baby, columns='도수')
print(baby_t)
#pie
baby_t.plot(kind='pie',autopct='%1.0f%%',subplots=True,legend=False)
plt.title("형제자매의 수")
plt.ylabel("")
plt.show(block=True)
plt.savefig("연습문제4.2.1.png")

#bar
baby_t.plot(kind='bar',legend=False)
plt.title("형제자매의 수")
plt.xlabel("")
plt.show(block=True)
plt.savefig("연습문제4.2.3.png")

######################### 4.3  #########################
phone = np.array([5,3,2,7,3,2,6,3,2,2,
                  5,4,8,3,5,4,4,6,2,6,
                  5,5,5,3,4,7,1,4,5,3])


#table
phone_t = pd.crosstab(index=phone, columns='도수')
print(phone_t)
#pie
phone_t.plot(kind='pie',autopct='%1.0f%%',subplots=True,legend=False)
plt.title("전화의 수")
plt.ylabel("")
plt.show(block=True)
plt.savefig("연습문제4.3.2.png")

#bar
phone_t.plot(kind='bar',legend=False)
plt.title("전화의 수")
plt.xlabel("")
plt.show(block=True)
plt.savefig("연습문제4.3.3.png")

######################### 4.4  #########################
letter = np.array([0,0,1,0,0,0,0,0,1,0,
                   0,1,0,2,3,2,1,1,0,1,
                   0,0,0,1,0,1,0,1,2,0,
                   2,0,0,1,1,2,1,3,1,1])

#table
letter_t = pd.crosstab(index=letter, columns='도수')
print(letter_t)
#pie
letter_t.plot(kind='pie',autopct='%1.0f%%',subplots=True,legend=False)
plt.title("글자의 수")
plt.ylabel("")
plt.show(block=True)
plt.savefig("연습문제4.4.2.png")

#bar
letter_t.plot(kind='bar',legend=False)
plt.title("글자의 수")
plt.xlabel("")
plt.show(block=True)
plt.savefig("연습문제4.4.3.png")

######################### 4.5  #########################
student = np.array([1,3,3,1,1,3,0,3,3,3,
                    2,1,1,1,2,4,1,1,1,1,
                    1,2,1,3,2,1,1,0,5,1])

#table
student_t = pd.crosstab(index=student, columns='도수')
print(student_t)
#pie
student_t.plot(kind='pie',autopct='%1.0f%%',subplots=True,legend=False)
plt.title("지각,결석한 학생의 수")
plt.ylabel("")
plt.show(block=True)
plt.savefig("연습문제4.5.2.png")

#bar
student_t.plot(kind='bar',legend=False)
plt.title("지각,결석한 학생의 수")
plt.xlabel("")
plt.show(block=True)
plt.savefig("연습문제4.5.3.png")


######################### 5.8  #########################
import stemgraphic
statistics = np.array([54,80,83,42,86,63,63,57,71,84,77,59,
                       90,73,81,76,56,81,85,51,94,66,73,88,
                       89,87,56,84,61,78,83,91,58,50,82])
#hist
plt.figure()
n, bins, patches = plt.hist(statistics, bins=[39.5,47.5,55.5,63.5,71.5,79.5,87.5,95.5],normed=True)
plt.show(block=True)

#leaf-stem plot
stemgraphic.stem_graphic(statistics)
plt.show()


######################### 5.10  #########################
n, bins, patches = plt.hist(statistics, bins=9,normed=True)
plt.show(block=True)

######################### 5.11  #########################
grade = np.array([190,119,114,176,135,178,158,160,147,194,
                 126,145,162,174,178,162,154,106,157,131,
                 182,152,136,165,161,95,115,184,166,115,
                 145,162,144,138,171,98,143,133,167,137])
#
n, bins, patches = plt.hist(grade, bins=[92.5,107.5,122.5,137.5,152.5,167.5,182.5,197.5],normed=True)
plt.show(block=True)
#
n, bins, patches = plt.hist(grade, bins=[90.5,100.5,110.5,120.5,130.5,140.5,150.5,160.5,170.5,180.5,190.5,200.5],normed=True)
plt.show(block=True)

#
stemgraphic.stem_graphic(grade)
plt.show()

######################### 5.13  #########################

income = np.array([749,776,813,585,649,679,760,751,767,642,
                   580,681,734,754,594,654,747,765,651,760])


n, bins, patches = plt.hist(income, bins=[575,625,675,725,775,825],normed=True)
plt.show(block=True)

n, bins, patches = plt.hist(income, bins=[550,650,750,850],normed=True)
plt.show(block=True)

######################### 5.14  #########################
math =  np.array [43,31,41,39,36,45,
                  38,44,29,35,29,41,
                  37,37,33,41,48,29,
                  35,36,28,31,37,49]

im = np.array([28,34,22,28,32,32,
               36,30,24,33,25,30,
               32,30,21,27,20,31,
               29,26])

n, bins, patches = plt.hist(im, bins=[20,25,30,35,40,45,50],normed=True)
plt.title("일반수학")
plt.show(block=True)

n1, bins1, patches1 = plt.hist(math, bins=[20,25,30,35,40,45,50],normed=True)
plt.title("공업수학")
plt.show(block=True)

#
x = [(bins[i]+bins[i+1])/2 for i in range(len(bins)-1)]
x1 = [(bins1[i]+bins1[i+1])/2 for i in range(len(bins1)-1)]

plt.plot(x,n,marker='o',label='일반수학')
plt.plot(x1,n1,marker='o',label='공업수학')
plt.legend(loc='upper right')
plt.show(block=True)

######################### 5.15  #########################
income1 = {"구분" : ['0~20', '20~40','40~60','60~80','80~100'],
           "고객수" : [65,88,42,27,18]}
pd_income1 = pd.DataFrame(income1)
pd_income1.plot.bar(legend=False)
plt.title('고객의 한달 소득')
plt.show(block=True)

######################### 5.16  #########################

weight = np.array([120,116,94,120,112,112,106,102,118,112,
                   116,98,116,114,120,124,112,122,110,84,
                   106,102,140,102,122,112,110,130,112,114,
                   108,110,116,118,118,108,102,110,104,112])

n, bins, patches = plt.hist(weight, bins=[80,90,100,110,120,130,140,150],normed=True)
plt.title('실험용 쥐 몸무게 자료')
plt.show(block=True)

######################### 5.17  #########################
accident = {"구분" : ['24이하', '24~49','50~74','75~99','100~149','150~199','200~249',"250이상"],
            "사상자" : [10,21,20,13,7,2,4,2]}
pd_accident = pd.DataFrame(accident)
pd_accident.plot.bar(legend=False)
plt.title('회오리바람에 의한 사상자의 수')
plt.show(block=True)

######################### 5.18  #########################

time = np.array([35,22,63,6,49,19,15,83,46,49,
                 16,31,24,36,68,42,57,64,29,8,
                 32,23,47,21,51,7,40,19,16,46,
                 108,33,55,32,22,36,25,27,37,58,
                 39,10,42,28,72,13,51,45,77,16])

n, bins, patches = plt.hist(time, bins=17,normed=True)
plt.title('히스토그램')
plt.show(block=True)

##
stemgraphic.stem_graphic(time)
plt.show()


######################### 5.19  #########################
oil = np.array([20,18,25,26,17,14,20,14,18,15,
                22,15,17,25,22,12,52,27,24,41,
                34,20,17,20,19,20,16,20,15,34,
                22,29,29,34,27,13,6,24,47,32,
                12,17,36,35,41,36,32,46,30,51])
stemgraphic.stem_graphic(oil)

######################### 5.21  #########################
data = np.array([193,198,200,202,203,203,205,205,206,207,
                 207,208,212,213,214,217,219,220,222,226,237])
stemgraphic.stem_graphic(data)

######################### 5.23  #########################
bigmac = np.array([3.4,2.6,3.0,3.8,4.0,3.9,3.1,1.5,3.4,2.2,
                   2.9,5.3,2.8,1.7,1.5,3.4,7.4,1.7,2.5,2.9,
                   2.8,1.6,2.7,3.5,7.2,2.3,2.2,3.1,2.0,2.7,
                   2.1,2.4,2.7,2.6,2.2,3.1,1.9,5.0,5.5,2.3,
                   2.0,4.0,2.7,1.8,2.8,3.4])

stemgraphic.stem_graphic(bigmac)
plt.show()

######################### 6.1  #########################
plan = np.array([3,2,1,3,3,3,1,3,3,3,3,2,3,1] )

t_plan = pd.crosstab(index=plan,columns='도수')
ft_plan = t_plan/len(plan)
ft_plan.plot(kind='pie',subplots=True,autopct='%1.0f%%')
ft_plan.plot(kind='bar',subplots=True)
plt.show(block=True)

######################### 6.3  #########################
import pandas as pd
survey = np.array([4,2,1,3,3,2,4,2,1,1,2,2,2,2,1,3,4,
                   1,4,4,1,3,2,4,1,4,3,3,1,1,1,2,1,1,
                   4,4,4,4,4,1,2,2,2,4,4,4,1,3,4,2,])
## table
survey_t = pd.crosstab(index=survey,columns='도수')
## bar graph
survey_t.plot(kind='bar',legend=False)
plt.xlabel(" ")
plt.show()
## pie graph
survey_t.plot(kind='pie',legend=False,subplots=True)
plt.ylabel(" ")
plt.show()

######################### 6.4  #########################
## 6.4.1
#S =1, P=2, B=3, H=4
info = np.array([1,2,1,3,2,3,4,3,4,1,
                 3,2,4,2,3,3,4,3,2,1,
                 2,3,2,1,4,3,4,2,1,3,
                 2,4,2,1,2,3,4,2,1,2,
                 4,2,1,3,2,4,1,3,3])
ind = ['S','P','B','H']
info_t = pd.crosstab(index=info, columns='도수')
info_t.index = ind
info_t

## 6.4.2
grade = np.array([3,3,4,1,4,3,3,4,3,3,
                  3,3,2,4,3,3,4,3,2,4,
                  4,2,4,3,1,1,3,4,3,2,
                  2,4,1,4,3,4,3,2,4,4,
                  3,3,2,2,2,4,3,2,3])

grade_t = pd.crosstab(index = grade, columns='도수')
grade_t.index = ['1학년','2학년','3학년','4학년']
grade_tf = grade_t / np.sum(grade_t)

grade_tf.plot(kind='bar',width=2,legend=False)
plt.xlabel(" ")
plt.xticks(rotation=360)
plt.show()

######################### 6.5  #########################
man_age = pd.DataFrame([40,4550,16830,6190,1140,330,160,10,20])
man_age_tf = man_age/np.sum(man_age)

man_age_tf.plot(kind='bar',width=2,legend=False)
plt.show()


######################### 6.12  #########################
carbon = np.array([0.07,0.07,0.12,0.95,0.35,0.13,0.06,0.72,0.13,0.17,
                   0.15,0.27,0.38,0.09,0.06,0.58,0.31,0.12,0.86,0.05,
                   0.06,0.20,0.39,0.12,0.07,0.14,1.13,0.10,0.15,0.20,
                   0.05,0.22,0.10,0.10,0.19,2.40,0.57,0.11,0.40,0.50,
                   0.14,0.12,0.08,0.29,0.09,2.70,0.12,0.11,0.05,0.22,
                   0.10])

n, bins, patches = plt.hist(carbon,bins=[0,0.1,0.2,0.3,0.4,0.5,0.6,1,3],normed=True)
plt.show()

######################### 6.13  #########################
cholesterol = np.array([239,212,249,227,218,310,281,330,226,233,
                        223,161,195,233,249,284,245,174,154,256,
                        196,299,210,301,199,258,205,195,227,244,
                        355,234,195,179,357,282,265,286,286,176,
                        195,163,297])
n, bins, patches = plt.hist(cholesterol,bins=[150,200,250,300,400],normed=True)
plt.show()

######################### 6.16  #########################
ozone = np.array([3.5,1.4,6.6,6.0,4.2,4.4,5.3,5.6,
                  6.8,2.5,5.4,4.4,5.4,4.7,3.5,4.0,
                  2.4,3.0,5.6,4.7,6.5,3.0,4.1,3.4,
                  6.8,1.7,5.3,4.7,7.4,6.0,6.7,11.7,
                  5.5,1.1,5.1,5.6,5.5,1.4,3.9,6.6,
                  6.2,7.5,6.2,6.0,5.8,2.8,6.1,4.1,
                  5.7,5.8,3.1,5.8,1.6,2.5,8.1,6.6,
                  9.4,3.4,5.8,7.6,1.4,3.7,2.0,3.7,
                  6.8,3.1,4.7,3.8,5.9,3.3,6.2,7.6,
                  6.6,4.4,5.7,4.5,3.7,9.4])

n, bins, patches = plt.hist(ozone,bins=12,normed=True)
x = [(bins[i]+bins[i+1])/2 for i in range(len(bins)-1)] # 꺽은선
w_bin = bins[1]-bins[0]
x.insert(0,x[0]-w_bin)
x.append(x[-1]+w_bin)
n = np.insert(n,0,0.0)
n = np.append(n,0.0)
plt.xlabel('ozone')
plt.ylabel('Frequency')
plt.title("Histogram of ozone")
plt.plot(x,n,'blue',marker='o')
plt.show()


######################### 6.17  #########################
acid = np.array([3.57, 3.80, 4.01, 4.01, 4.05, 4.05, 4.58, 4.60, 4.61, 4.61, 4.62, 4.62,
                 4.12, 4.18, 4.20, 4.21, 4.27, 4.28, 4.65, 4.70, 4.70, 4.70, 4.70, 4.72,
                 4.30, 4.32, 4.33, 4.35, 4.35, 4.41, 4.78, 4.78, 4.80, 5.07, 5.20, 5.26,
                 4.50, 4.51, 4.52, 4.52, 4.52, 4.57, 5.41, 5.48])

n, bins, patches = plt.hist(acid,bins=[3.4,3.6,3.8,4.0,4.2,4.4,4.6,4.8,5.0,5.2,5.4,5.6])
x = [(bins[i]+bins[i+1])/2 for i in range(len(bins)-1)] # 꺽은선
w_bin = bins[1]-bins[0]
x.insert(0,x[0]-w_bin)
x.append(x[-1]+w_bin)
n = np.insert(n,0,0.0)
n = np.append(n,0.0)
plt.xlabel('acid')
plt.ylabel('Frequency')
plt.title("Histogram of acid")
plt.plot(x,n,'blue',marker='o')
plt.show()

