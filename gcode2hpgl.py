# -*- coding: utf-8 -*-


# Дорогие друзья, я не программист, а просто любитель
# Я во многом не разбираюсь в программировании, потому тут может быть много говно-кода
# Но оно как-то работает. Не кидайте тапками :)

from colorama import init     # Цветные буковки
from termcolor import colored # Тоже цветные буковки
init()                        # Надо, чтобы под виндой были цветные буковки
import pyfiglet               # Красивые буковки
import os
import shutil


logo = pyfiglet.figlet_format("gcode 2 hpgl") #Лого
print(colored((logo), 'yellow'))
print(colored("GCODE в HPGL конвертер. Для плоттеров и станков с ЧПУ (Suda, Cipher, Mult-CAM)", 'yellow'))
print(colored("Автор программы: https://github.com/daneelka11/", 'yellow'))
print(colored("", 'red'))
print(colored("Внимание! Это бета-версия и не отображает финальное качество программы.", 'red'))
print(colored("Программа поставляется 'Как есть' и автор не несет ответственности за возможный", 'red'))
print(colored("принесённый ушерб. Используйте на свой страх и риск!", 'red'))
print("")
print("")
while True:
    # ШАГ 1
    print(colored("Шаг 1. Укажите ПУТЬ к исходному GCODE файлу ", 'yellow') + colored("(с знаком \ в конце)", 'red')) 
    pyt_gcode = str(input("")) # Просим ввод пути к файлу gcode
    #--=-=-=-=-=- ПРОВЕРКИ НА СУЩЕСТВОВАНИЕ ДИРЕКТОРИИ/ТИП (ФАЙЛ/ДИРЕКТОРИЯ) -=-=-=-=-=--
    if(os.path.exists(pyt_gcode) == False): # Если путь не существует
        os.system('cls' if os.name == 'nt' else 'clear') #Чистим терминал
        print(colored("Указанный путь не существует. Повторите попытку!", 'red')) # Быкуем
        continue # Начинаем по новой
    if (os.path.isfile(pyt_gcode) == True): # Если это файл, а не папка
        os.system('cls' if os.name == 'nt' else 'clear') #Чистим терминал
        print(colored("Вы указали файл, а не директорию где находиться GCODE (.gcode) файл.", 'red')) # Быкуем
        print(colored("Повторите попытку и укажите директорию!", 'red')) # Быкуем
        print("")
        continue # Начинаем по новой 
    os.system('cls' if os.name == 'nt' else 'clear') #Чистим терминал
    
    
    # ШАГ 2
    print(colored("Шаг 2. Укажите название GCODE файла. ", 'yellow') + colored("(без расширения .gcode)", 'red'))
    name_gcode = str(input(""))  # Просим ввод пути к директории для сохранения
    gcodefile = pyt_gcode + name_gcode + ".gcode" # Находим полный путь к GCODE файлу и записываем в переменную gcodefile
    #--=-=-=-=-=- ПРОВЕРКИ НА СУЩЕСТВОВАНИЕ ДИРЕКТОРИИ/ТИП (ФАЙЛ/ДИРЕКТОРИЯ) -=-=-=-=-=--
    if(os.path.exists(gcodefile) == False): # Если файл не существует
        os.system('cls' if os.name == 'nt' else 'clear') #Чистим терминал
        print(colored("Указанный файл не существует. Повторите попытку!", 'red')) # Быкуем
        print("")
        continue # Начинаем по новой
    os.system('cls' if os.name == 'nt' else 'clear') #Чистим терминал

    
    # ШАГ 3
    print(colored("Шаг 3. Укажите путь к директории в которую необходимо сохранить HPGL файл (.plt) ", 'yellow') + colored("(с знаком \ в конце)", 'red')) 
    pyt_HPGL = str(input("")) # Просим ввод пути к сохраняемому файлу
    #--=-=-=-=-=- ПРОВЕРКИ НА СУЩЕСТВОВАНИЕ ДИРЕКТОРИИ/ТИП (ФАЙЛ/ДИРЕКТОРИЯ) -=-=-=-=-=--
    if(os.path.exists(pyt_gcode) == False): # Если путь не существует
        os.system('cls' if os.name == 'nt' else 'clear') #Чистим терминал
        print(colored("Указанный путь не существует. Повторите попытку!", 'red')) # Быкуем
        continue # Начинаем по новой
    if (os.path.isfile(pyt_gcode) == True): # Если это файл, а не папка
        os.system('cls' if os.name == 'nt' else 'clear') #Чистим терминал
        print(colored("Вы указали файл, а не директорию, куда необходимо сохранить HPGL (.plt) файл", 'red')) # Быкуем
        print(colored("Повторите попытку и укажите директорию!", 'red')) # Быкуем
        print("")
        continue # Начинаем по новой 
    os.system('cls' if os.name == 'nt' else 'clear') #Чистим терминал


    #Процесс пост-процессинга
    print(colored("Копируем файл...", 'yellow'))
    pltfile = pyt_HPGL + name_gcode + ".plt"
    shutil.copy(gcodefile, pltfile) #Копируем gcode, меняем расширение на plt
    print(colored("Файл скопирован по пути: " + pltfile, 'green'))
    print(colored("Начинаю пост-процессинг...", 'yellow'))

    f = open(pltfile, 'r+')     # Открываем файл
    code = f.read().splitlines() # Все содержимое пишем в список "code", ух костыыыль...

    count = 0                    # Переменная для подсчёта кол-ва строк
    lastz = 0
    lastx = 0
    lasty = 0
    for line in code: # Считаем кол-во строк
        inp = code[count]
        ps = ''
        if (inp.find("X") > -1 or inp.find("Y") > -1 or inp.find("Z") > -1):
        
            if (inp.find("X") > -1):
                xc = inp.find("X") + 1
                
                if (inp.find("Y") > -1):
                    yc = inp.find("Y")
                    ps = "PU" + str(round(float(inp[xc:yc]) * 100))
                    lastx = round(float(inp[xc:yc]) * 100)
                    
                    if(inp.find("Z") > -1):
                        yc = inp.find("Y") + 1 
                        zc = inp.find("Z")
                        ps = ps + "," + str(round(float(inp[yc:zc]) * 100))
                        lasty = round(float(inp[yc:zc]) * 100)
                        if(inp.find("F") > -1):  #Если после Z есть ещё и F
                            zc = inp.find("Z") + 1
                            fc = inp.find("F")
                            ps = ps + "," + str(round(float(inp[zc:fc]) * -100)) + ";"
                            lastz = round(float(inp[zc:fc]) * 100)
                            code[count] = ps
                            count = count + 1
                            continue
                            
                        else:
                            zc = inp.find("Z") + 1
                            fc = len(inp)
                            ps = ps + "," + str(round(float(inp[zc:fc]) * -100)) + ";"
                            lastz = str(round(float(inp[zc:fc]) * -100))
                            code[count] = ps
                            count = count + 1
                            continue
                    else:
                        if(inp.find("F") > -1): # И после Y - F
                            yc = inp.find("Y") + 1
                            fc = inp.find("F")
                            ps = ps + "," + str(round(float(inp[yc:fc]) * 100))
                            ps = ps + "," + str(lastz) + ";"
                            lasty = round(float(inp[yc:fc]) * 100)
                            code[count] = ps
                            count = count + 1
                            continue
                        else:
                            yc = inp.find("Y") + 1
                            zc = len(inp)
                            ps = ps + "," + str(round(float(inp[yc:zc]) * 100))
                            ps = ps + "," + str(lastz) + ";"
                            lasty = round(float(inp[yc:zc]) * 100)
                            code[count] = ps
                            count = count + 1
                            continue
                        
                        
                        
                else: #Если есть только X
                    if(inp.find("F") > -1): # И после X - F
                        fc = inp.find("F")
                        ps = "PU" + str(round(float(inp[xc:fc]) * 100))
                        ps = ps + "," + str(lasty) + "," + str(lastz) + ";"
                        lastx = str(round(float(inp[xc:fc]) * 100))
                        code[count] = ps
                        count = count + 1
                        continue
                    else: 
                        yc = len(inp)
                        ps = "PU" + str(round(float(inp[xc:yc]) * 100))
                        ps = ps + "," + str(lasty) + "," + str(lastz) + ";"
                        lastx = str(round(float(inp[xc:yc]) * 100))
                        code[count] = ps
                        count = count + 1
                        continue
            
            
            
            
            if (inp.find("Y") > -1):
                yc = inp.find("Y") + 1
                
                if (inp.find("F") > -1):
                    fc = inp.find("F")
                    ps = "PU" + str(lastx) + "," + str(round(float(inp[yc:fc]) * 100)) + "," + str(lastz) + ";"
                    lasty = round(float(inp[yc:fc]) * 100)
                    code[count] = ps
                    count = count + 1
                    continue
                else:
                    ya = len(inp)
                    ps = "PU" + str(lastx) + "," + str(round(float(inp[yc:ya]) * 100)) + "," + str(lastz) + ";"
                    lasty = round(float(inp[yc:ya]) * 100)
                    code[count] = ps
                    count = count + 1
                    continue
            
            if (inp.find("Z") > -1):
                zc = inp.find("Z") + 1
                
                if (inp.find("F") > -1):
                    fc = inp.find("F")
                    ps = "PU" + str(lastx) + "," + str(lasty) + "," + str(round(float(inp[zc:fc]) * -100)) + ";"
                    lastz = round(float(inp[zc:fc]) * -100)
                    code[count] = ps
                    count = count + 1
                    continue
                else:
                    za = len(inp)
                    ps = "PU" + str(lastx) + "," + str(lasty) + "," + str(round(float(inp[zc:za]) * -100)) + ";"
                    lastz = round(float(inp[zc:za]) * -100)
                    code[count] = ps
                    count = count + 1
                    continue
               
                
        else:
            code[count] = ""
        count=count+1  

    code.insert(0, 'IN;MK;PU;')     #Добавляем команду инициализация процесса черчения в список
    code.insert(len(code) + 1, '!PG;')
    print(colored("Начинаю запись в файл...", 'yellow'))
    f.seek(0)
    for line in code:
        f.write(line + '\n')
    print(colored("Готово!", 'green'))
    f.close()
    print("")
    print("")
    print(colored("Выберите действие:", 'yellow'))
    print(colored("0 - Закрыть программу", 'yellow'))
    print(colored("1 - Начать заново", 'yellow'))
    act = int(input())
    if(act == 0):
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear') #Чистим терминал
    

    
    
    
    