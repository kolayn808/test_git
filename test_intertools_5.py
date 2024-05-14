import random
import time
import matplotlib.pyplot as plt
timelist=[]

spisok_quantity_elements = []
spisok_half_time = []
for quantity_elements in range(10,110,10):
    spisok_quantity_elements.append(quantity_elements)
    for g in range(100):
        start = time.perf_counter()
        probability_accept = 0.2

        a= 0

        probability_list = []

        for i in range(quantity_elements):
            probability_list.append(round(random.uniform(0.01,0.99),2))

        print(probability_list)

        print(f"Список вероятностей доступности данных для агентов сети {probability_list}")

        temporary_list = []

        k=0
        clast = 0
        claster = []
        claster_dict=[]
        global j

        while probability_list:
            j = 0
            if not probability_list:
                break

            k += 1
            probability_composition = probability_list[0]
            while probability_composition >= probability_accept and probability_list[j] != probability_list[-1]:

                j += 1
                probability_composition = probability_composition * (1 - probability_list[j])


            for z in range(0, (j+1)):
                temporary_list.append(probability_list[z])

                # clast += 1
                claster = (temporary_list)
            print(f"Кластер {k}:", claster)

            claster_dict.append(claster)
            claster.clear()
            del probability_list[0:j+1]

        finish = time.perf_counter()
        time_itog = finish - start
        print("Время работы программы: ", time_itog)
        timelist.append(time_itog)
        half_time = sum(timelist)/len(timelist)

    spisok_half_time.append(half_time)

print(spisok_half_time)
spisok_j =[]
spisok_jj = []




fig = plt.figure(facecolor='white')
for j in timelist:

    spisok_j.append(j)
for i in range(len(timelist)):
    spisok_jj.append(i)

print(spisok_jj)

plt.plot( spisok_half_time, spisok_quantity_elements)
plt.xlabel('Среднее время работы алгоритма, с')
plt.ylabel('Количество блоков данных, шт')

plt.grid(True)
plt.show()
