#НАЗВАНИЕ ПРОЕКТА:
#шифровка и рассшифровка сообщений.


#ЦЕЛЬ ПРОЕКТА:
#создать программу которая будет шифровать 
#и рассшифровывать сообщения с помошью ШИФРА ЦЕЗАРЯ.


#ЧТО ТАКОЕ ШИФР ЦЕЗАРЯ:
#шифр цезаря-Шифр Цезаря — это моноалфавитная кодировка,
#представляющая собой тип шифра подстановочного типа, 
#отличающийся от других систем кодирования тем, что в открытом тексте каждая буква заменяется другой, 
#взятой из алфавита и смещенной на определенное количество позиций.


#ЧТО ТАКОЕ ЮНИКОД:
#стандарт кодирования символов, включающий в себя знаки почти всех письменных языков мира[2]. 
# В настоящее время стандарт является преобладающим в Интернете. 
#в таблице юникода 256 символов.


#ЧТО ДЕЛАЮТ ФУНКЦИИ CHR И ORD:
#Встроенная функция Python chr() используется для преобразования целого числа в символ,
#функция ord() используется для обратного, т. е. преобразования символа в целое число.


#ДЛЯ ЧЕГО МОЖЕТ ПРИГОДИТЬСЯ ШИФР ЦЕЗАРЯ:
#Шифры применяются для тайной переписки дипломатических представителей со своими правительствами, 
#в вооружённых силах для передачи текста секретных документов по техническим средствам связи, 
#банками для обеспечения безопасности транзакций, а также некоторыми интернет-сервисами по различным причинам.


#КАКИЕ ЕЩЕ ЕСТЬ ШИФРЫ :
#АЗБУКА МОРЗЕ-буквы алфавита, цифры, знаки препинания и другие символы представляются в виде последовательностей 
#коротких и длинных сигналов, называемых точками и тире[1].


#ШИФР ВИЖЕНЕРА-это метод шифровки, в котором используются различные «шифры Цезаря» на основе букв в ключевом слове.


#ШИФР ЭНИГМЫ-это тип коммутативного шифра, который шифрует буквы, 
#заменяя их другими буквами. Шифр Энигма шифрует 26 символов, от "A" до "Z".

action=input("введите действие шифровка/рассшифровка ").upper() #запрашиваем действие 
if action=="ШИФРОВКА":
    step=int(input("введите шаг для шифровки ")) # запрашиваем шаг шифровки
    message=input("введите сообщение для шифровки ") #запрашиваем сообщение для шифровки
    for i in message: #проходимся циклом по сообщению
        result=int(ord(i))-step #записываем в переменную result наше сообшение преобразрванное в целое число с помощью ord и отнимаем шаг шифровки
        print(chr(result), sep="\n", end="") #выводим result преобразованный из целых чисел с символы  с помщью chr
elif action=="РАССШИФРОВКА":
    step=int(input("введите шаг который вы выбирали при шифровке"))# запрашиваем шаг рассшифровки
    message=input("введите сообщение для рассшифровки ") #запрашиваем сообщение для рассшифровки
    for i in message:#проходимся циклом по сообщению
        result=int(ord(i))+step#записываем в переменную result наше сообшение преобразрванное в целое число с помощью ord и  прибавляем шаг рассшифровки
        print(chr(result), sep="\n", end="") #выводим result преобразованный из целых чисел с символы с помощью chr

#ЧЕМУ Я НАУЧИЛСЯ ДЕЛАЯ ЭТОТ ПРОЕКТ:
#Я научился пользоваться командами chr и ord
#узнал что такое таблица юникода 
#узнал что такое шифр цезаря
