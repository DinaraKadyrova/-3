import time

max_bufer_len = 100  # максимальный размер рабочего буфера
bufer_len = 1  # размер буфера чтения
work_bufer = ""  # рабочий буфер
n = 0  # счётчик длины слова
m = 0  # максимальная длина слова

try:
    with open("laba2.txt", "r") as file:  # открываем файл
        print("Результат работы программы:")
        bufer = file.read(bufer_len)  # читаем первый блок

        if not bufer:  # если файл пустой
            print("\nФайл text.txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")

        k = int(input('Введите число: '))
        while bufer:  # пока файл не пустой
            #print(bufer)

            if bufer.isalpha():  # обрабатываем текущий блок
                n += 1
                if n>m:
                    m = n
                work_bufer += bufer
            else:
                n = 0
                work_bufer += bufer
            
            if bufer.find(".") >= 0 or bufer.find("!") >= 0 or bufer.find("?") >= 0:  # Если символ-окончание предложения
                if m > k:  # если максимальная длина слова больше введёного числа
                    print(work_bufer)  # Печатаем предложение и готовим новый цикл
                    m = 0  # обнуляем максимальное значение
                work_bufer = ""
            bufer = file.read(bufer_len)  # читаем очередной блок

            if len(work_bufer) >= max_bufer_len and bufer.find(".") < 0 and bufer.find("!") < 0 and bufer.find("?") < 0:  # Если буфер переполнен и нет окончания предложения
                print("\nФайл text.txt не содержит знаков окончания предложения и максимальный размер буфера превышен.\nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")

        if len(work_bufer) > 0:  # Если буфер переполнен и нет окончания предложения
            print("\nХвост файла text.txt не содержит знаков окончания предложения \nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
print("\nВремя работы программы:  ", time.process_time(), "seconds")