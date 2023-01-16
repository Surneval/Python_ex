#38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)
text = "Привет, как дела? абв мабвб ввввв ваааабв, абв, вабв!"
text = text.split()
text_new = []
for i in range(len(text)):
    if 'абв' not in text[i]:
        text_new.append(text[i])
print(text_new)
