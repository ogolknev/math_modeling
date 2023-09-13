import matplotlib.pyplot as plt

# Функция чтения данных из указанного файла
def data_reader(path: str):
    data_obj = open(path)
    data_str = data_obj.readline()
    data_list = list()
    cntr = 0
    while data_str:
        data_list.append(list())
        data_list[cntr].append(list(float(x) for x in ''.join(data_str).split(' ')))
        print(''.join(data_str.split('\n')).split(' '))
        data_str = data_obj.readline()
        data_list[cntr].append(list(float(y) for y in ''.join(data_str).split(' ')))
        data_str = data_obj.readline()
        data_str = data_obj.readline()
        cntr += 1
    data_obj.close()
    return data_list

# Функция вывода выбранных графиков на экран
def data_drawer(path: str, mode):
    data = data_reader(path)
    for i in range(len(data)):
        if mode == 'a' or i + 1 in list(int(el) for el in mode.split(' ')):
            plt.scatter(data[i][0], data[i][1])
    plt.show()

data_drawer('data.txt', input('Ведите количество или номер(a) графика: '))