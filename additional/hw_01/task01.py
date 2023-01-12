#HOME_WORK_1
#1.Клиент покупает кофе в кафе. За каждые 6 чашек, 1 чашка даётся в качестве бонуса.
#Задача: запросить у пользователя кол-во чашек на покупку, вычислить полагающееся кол-во бонусных чашек кофе и вывести это число на консоль.

cups_bought = int(input("How many cups of coffee have you already biught? >> "))
prize = 6
bonus_cups = cups_bought // prize
print(f"Ypu have already biught {cups_bought} cups of coffee, you can get {bonus_cups:1.0f} bonus cups")