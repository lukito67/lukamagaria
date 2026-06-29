#1)დაალაგე ეს სია ზრდადობით: numbers = [9, 2, 7, 1, 5] და დააბრუნე საპირისპირო მიმართულებით.
num = [9,2,7,1,5]
num.sort()
num.reverse()
print(num)



#2) words = ["I", "love", "Python"]გადააქციე ერთ სტრიქონად, რომ შედეგი იყოს:I love Python
words = ["i","love","python"]
worlds = " ".join(words)
print(worlds)



#3)text = "dog cat bird" გაყავი სიტყვებად და დაბეჭდე მიღებული სია.
text = "dog cat bird"
chickenjokey = text.split()
print(chickenjokey)



#4) შეიყვანე სიტყვა და:დაბეჭდე მთლიანად დიდი ასოებით.შემდეგ დაბეჭდე მთლიანად პატარა ასოებით.
dada = "stick"
mama = dada.upper()
print(mama)
hole = mama.lower()
print(hole)



#5) text = "Programming" იპოვე ასო "g"-ის პირველი ინდექსი. დათვალე რამდენჯერ გვხვდება ასო "a". 
text = "programming"
print(text.find("g"))
print(text.count("a"))