#1) მომხმარებელს შემოაყვანინეთ რიცხვი და შეამოწმეთ დადებითია თუ უარყოფითი.
i = int(input("enter the number"))
if i > 0:
    print("your number is positeve")
elif i < 0:
    print("your number is nagiteve")
else:
    print("your number is 0")



#2)მომხარებელს შემოაყვანინეთ ასაკი და შეამოწმეთ სრულწლოვანი არის თუ არა .
l = int(input("enter your age"))
if l > 18:
    print("you are an adult")
elif l < 19:
    print("you are a minor")
else:
    print("enter yor age")



#3)მომხმარებლს შემოაყვანინეთ რიცხვი და თუ 10 ზე მეტია შედეგად გაამრავლეთ 2 ზე.
ove = int(input("enter the number"))
if ove > 10:
    print(ove * 2)
else:
    print(ove)
