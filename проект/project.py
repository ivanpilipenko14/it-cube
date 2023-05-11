alfavit_EU="!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~" # создаем  английский алфавит
alfavit_RU="!#$%&'()*+,-./0123456789:;<=>?@абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ[\]^_`{|}~"  # создаем  русский алфавит
action=input("введите действие которое вы хотите совершить(шифровка/рассшифровка)  ").upper() # запрашиваем действие у пользователя 
itog="" #создаем отдельную переменную которая будет принимать в себя готовое сообщение
if action == "ШИФРОВКА":   
    language=input("выберете язык (RU/EU)  ").upper() #запрашиваем у пользователя язык сообщения
    if language == "RU":
        message=input("введите сообщение для шифровки  ") # запрашиваем сообщение  для шифровки и переводим в верхний регистр 
        step=int(input("введите шаг шифровки  ")) # запрашиваем шаг шифровки
        for i in message: #проходимся циклом по нашему сообщению
           plase = alfavit_RU.find(i) # создаем цикл for,определяем место букв в нашем списке alfavit, после чего определяем их новые места:
           new_plase = plase + step #узнаем новое место
           if i in alfavit_RU: 
                itog += alfavit_RU[new_plase] #записываем наше сообщение уже в зашифрованном виде и выводим его
           else:
                itog += i
    if language == "EU":
        message=input("введите сообщение для шифровки  ") # запрашиваем сообщение  для шифровки и переводим в верхний регистр 
        step=int(input("введите шаг шифровки  ")) # запрашиваем шаг шифровки
        for i in message:
            plase = alfavit_EU.find(i)
            new_plase = plase + step
            if i in alfavit_EU:
               itog += alfavit_EU[new_plase]
            else:
               itog += i
print (itog)
    
if action == "РАССШИФРОВКА":
    language=input("выберете язык (RU/EU)  ").upper()
    if language == "RU":
        message=input("введите сообщение для рассшифровки  ")
        step=int(input("введите шаг для рассшифровки(который вы выбирали при шифровке только со знаком минуса)  "))
        for i in message:
            plase = alfavit_RU.find(i)
            new_plase = plase + step
            if i in alfavit_RU:
                itog += alfavit_RU[new_plase]
            else:
                itog += i
    if language == "EU":
        message=input("введите сообщение для рассшифровки  ")
        step=int(input("введите шаг для рассшифровки(который вы выбирали при шифровке только со знаком минуса)  "))
        for i in message:
            plase = alfavit_EU.find(i)
            new_plase = plase + step
            if i in alfavit_EU:
                itog += alfavit_EU[new_plase]
            else:
                itog += i
print (itog)
