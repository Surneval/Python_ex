#3. На ферме есть куры, коровы и свиньи. У курицы две ноги, у свиньи - четыре, у коровы - четыре. Запросить у пользователя (фермера) ввод кол-ва кур, свиней и коров, просуммировать кол-во ног всех животных и вывести результат на консоль.
try:
    chicken = int(input("Enter a number of chicken >> "))
    cow = int(input("Enter a number of cows >> "))
    pigs = int(input("Enter a number of pigs >> "))
except (ValueError, TypeError):
    print("Input a number")
chicken_leg = 2
coe_leg = 4
pig_leg = 4

all_legs = chicken * chicken_leg + cow * coe_leg + pigs * pig_leg

print(f"all together you have {all_legs:1.0f} legs")