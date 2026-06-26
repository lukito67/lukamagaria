#4) შექმენით ცარიელი ლისტი. მომხმარებელს for ციკლის გამოყენებით 5-ჯერ შემოატანინეთ სიტყვა და თითოეული append()
#  ფუნქციის გამოყენებით დაამატეთ ლისტში. ბოლოს for ციკლით დაბეჭდეთ ყველა ელემენტი.
list = []
for i in range(5):
    word = input("enter a word")
    list.append(word)
for word in list:
        print(word)



#5) შექმენით ლისტი რიცხვებით. for ციკლის გამოყენებით იპოვეთ ყველა რიცხვის ჯამი.

list2 = [1,2,3,4,5,6,7,8,9]
mama = 0
for love in list2:
      mama = mama + love
      print(mama)



#6) მომხმარებელს for ციკლის გამოყენებით 5-ჯერ შემოატანინეთ რიცხვი, დაამატეთ ისინი ლისტში
#  და ბოლოს for ციკლით დაბეჭდეთ თითოეული ელემენტი და len() ფუნქციის გამოყენებით ლისტის სიგრძე.
list3 = []
for l in range(5):
      kaka = int(input("enter a number"))
      list3.append(kaka)
      for kaka in list3:
            print(kaka)
print(len(list3))



#8) მომხმარებელს შემოატანინეთ რიცხვი და for ციკლის გამოყენებით დაბეჭდეთ ამ რიცხვის გამრავლების ტაბულა 1-დან 10-მდე.
nana = int(input("enter a number"))
for i in range(1,11):
      print(nana * i)