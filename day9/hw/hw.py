    #1)შემოიყვანეთ რიცხვი და შეამოწმეთ კენტია თუ ლუწი
i = int(input("enter a number: "))
if i % 2 == 0:
    print("ლუწია")
if i % 2 == 1:
    print("კენტია")
else:
    print("enter a number")



    #2) დაწერეთ კოდი რომელიც იქნება შუქნიშანის მსგავსი სისტემა, თუ სიტყვა არის 'მწვანე' გამოიტანეთ 'წადი',
    #  თუ ფერი არის ყვითელი მაშინ გამოიტანე 'მოემზადე', სხვა შემთხვევაში, ანუ წითელზე 'გაჩერდი'
love = str(input("enter a color: "))
if love == ("red"):
    print("stop")
elif love == ("green"):
    print("go")
elif love == ("yellow"):
    print("get ready")
else:
    print("enter colors: red,yellow,green")



    #3)მომხმარებელს შემოატანინეთ რიცხვი და შეამოწმეთ მომხმარებლის შემოტანილი რიცხვი 10 - ს უდრის თუ არა,
    #  თუ უდრის 10 - ს მაშინ დაბეჭდეთ, რომ  ‘რიცხვი არის 10 ის ტოლი’, თუ არ უდრის მაშინ ‘რიცხვი არ არის 10 ის ტოლი’.
u = int(input("enter a number: "))
if u == 10:
    print("your number equals 10")
elif u != 10:
    print("your number does not equals 10")
else:
    print("enter a number")