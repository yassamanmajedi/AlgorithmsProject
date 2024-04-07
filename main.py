from tkinter import *
from tkinter import ttk
import timeit
from data import data
from double1 import double1
from str1 import str1
from data1 import data1
from bubblesort import bubble_sort
from insertionsort import insertion_sort
from selectionsort import selection_sort
from quicksort import quick_sort
from mergesort import merge_sort
from countingsort import counting_sort
from radixsort import radix_sort
from heapsort import heap_sort

root = Tk()
root.title("sorting performances")
root.maxsize(2000, 2000)
root.config(bg="black")
algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'insertion sort', 'selection sort', 'heap sort', 'quick sort', 'merge sort',
             'counting sort', 'radix sort']


def sort():
    if algo_menu.get() == 'Bubble Sort':
        start = timeit.default_timer()
        bubble_sort(data)
        print(data)
        bubble_sort(double1)
        print(double1)
        bubble_sort(str1)
        print(str1)
        stop = timeit.default_timer()
        print('Time of my algorithm for sample: ', stop - start)
        start1 = timeit.default_timer()
        data.sort()
        double1.sort()
        str1.sort()
        stop1 = timeit.default_timer()
        print('Time of optimized algorithm for sample: ', stop1 - start1)
        time1 = stop - start
        time2 = stop1 - start1
        if time1 > time2:
            print("optimized algorithm has better performance")
            my_lable = Label(root, text="optimized algorithm has better performance and "
                                        f"my algorithm time is: {time1} and "
                                        f"the optimized algorithm is: {time2}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)
        else:
            print("my written algortihm has better performance")
            my_lable = Label(root, text="my algorithm has better performance and "
                                        f"my algorithm time is: {time1} and "
                                        f"the optimized algorithm is: {time2}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)

    elif algo_menu.get() == 'insertion sort':
        start = timeit.default_timer()
        insertion_sort(double1)
        print(double1)
        insertion_sort(data)
        print(data)
        insertion_sort(str1)
        print(str1)
        stop = timeit.default_timer()
        print('Time: ', stop - start)
        start1 = timeit.default_timer()
        data.sort()
        double1.sort()
        str1.sort()
        stop1 = timeit.default_timer()
        print('Time of optimized algorithm: ', stop1 - start1)
        time3 = stop - start
        time4 = stop1 - start1
        if time3 > time4:
            print("optimized algorithm has better performance")
            my_lable = Label(root, text="optimized algorithm has better performance and "
                                        f"my algorithm time is: {time3} and "
                                        f"the optimized algorithm is: {time4}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)
        else:
            print("my written algortihm has better performance")
            my_lable = Label(root, text="my algorithm has better performance and "
                                        f"my algorithm time is: {time3} and "
                                        f"the optimized algorithm is: {time4}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)
    elif algo_menu.get() == 'selection sort':
        start = timeit.default_timer()
        selection_sort(data)
        print(data)
        selection_sort(double1)
        print(double1)
        selection_sort(str1)
        print(str1)
        stop = timeit.default_timer()
        print('Time: ', stop - start)
        start1 = timeit.default_timer()
        data.sort()
        double1.sort()
        str1.sort()
        stop1 = timeit.default_timer()
        print('Time of optimized algorithm: ', stop1 - start1)
        time5 = stop - start
        time6 = stop1 - start1
        if time5 > time6:
            print("optimized algorithm has better performance")
            my_lable = Label(root, text="optimized algorithm has better performance and "
                                        f"my algorithm time is: {time5} and "
                                        f"the optimized algorithm is: {time6}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)
        else:
            print("my written algortihm has better performance")
            my_lable = Label(root, text="my algorithm has better performance and "
                                        f"my algorithm time is: {time5} and "
                                        f"the optimized algorithm is: {time6}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)
    elif algo_menu.get() == 'heap sort':
        start = timeit.default_timer()
        heap_sort(data)
        print(data)
        heap_sort(double1)
        print(double1)
        heap_sort(str1)
        print(str1)
        stop = timeit.default_timer()
        print('Time of my algorithm: ', stop - start)
        start1 = timeit.default_timer()
        data.sort()
        double1.sort()
        str1.sort()
        stop1 = timeit.default_timer()
        print('Time of optimized algorithm: ', stop1 - start1)
        time7 = stop - start
        time8 = stop1 - start1
        if time7 > time8:
            print("optimized algorithm has better performance")
            my_lable = Label(root, text="optimized algorithm has better performance and "
                                        f"my algorithm time is: {time7} and "
                                        f"the optimized algorithm is: {time8}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)
        else:
            print("my written algortihm has better performance")
            my_lable = Label(root, text="my algorithm has better performance and "
                                        f"my algorithm time is: {time7} and "
                                        f"the optimized algorithm is: {time8}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)
    elif algo_menu.get() == 'quick sort':
        start = timeit.default_timer()
        quick_sort(data, 0, len(data) - 1)
        print(data)
        quick_sort(double1, 0, len(double1) - 1)
        print(double1)
        quick_sort(str1, 0, len(str1) - 1)
        print(str1)
        stop = timeit.default_timer()
        print('Time: ', stop - start)
        start1 = timeit.default_timer()
        data.sort()
        double1.sort()
        str1.sort()
        stop1 = timeit.default_timer()
        print('Time: ', stop1 - start1)
        time9 = stop - start
        time10 = stop1 - start1
        if time9 > time10:
            print("optimized algorithm has better performance")
            my_lable = Label(root, text="optimized algorithm has better performance and "
                                        f"my algorithm time is: {time9} and "
                                        f"the optimized algorithm is: {time10}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)
        else:
            print("my written algortihm has better performance")
            my_lable = Label(root, text="my algorithm has better performance and "
                                        f"my algorithm time is: {time9} and "
                                        f"the optimized algorithm is: {time10}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)
    elif algo_menu.get() == 'merge sort':
        start = timeit.default_timer()
        merge_sort(data, 0, len(data) - 1)
        print(data)
        merge_sort(double1, 0, len(double1) - 1)
        print(double1)
        merge_sort(str1, 0, len(str1) - 1)
        print(str1)
        stop = timeit.default_timer()
        print('Time of my algorithm: ', stop - start)
        start1 = timeit.default_timer()
        data.sort()
        str1.sort()
        double1.sort()
        stop1 = timeit.default_timer()
        print('Time of optimized algorithm: ', stop1 - start1)
        time11 = stop - start
        time12 = stop1 - start1
        if time11 > time12:
            print("optimized algorithm has better performance")
            my_lable = Label(root, text="optimized algorithm has better performance and "
                                        f"my algorithm time is: {time11} "
                                        f"the optimized algorithm time is: {time12}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)
        else:
            print("my written algortihm has better performance")
            my_lable = Label(root, text="my algorithm has better performance and "
                                        f"my algorithm time is: {time11} "
                                        f"the optimized algorithm time is: {time12}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)
    elif algo_menu.get() == 'counting sort':
        start = timeit.default_timer()
        print(counting_sort(data1))
        stop = timeit.default_timer()
        print('Time: ', stop - start)
        start1 = timeit.default_timer()
        data1.sort()
        stop1 = timeit.default_timer()
        time13 = stop - start
        time14 = stop1 - start1
        print('optimized time: ', stop1 - start1)
        if time13 > time14:
            print("optimized algorithm has better performance")
            my_lable = Label(root, text="optimized algorithm has better performance and "
                                        f"my algorithm time is: {time13} and "
                                        f"the optimized algorithm is: {time14}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)
        else:
            print("my written algortihm has better performance")
            my_lable = Label(root, text="my algorithm has better performance and "
                                        f"my algorithm time is: {time13} and "
                                        f"the optimized algorithm is: {time14}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)

    else:
        start = timeit.default_timer()
        print(radix_sort(data1))
        stop = timeit.default_timer()
        print('Time: ', stop - start)
        start1 = timeit.default_timer()
        data1.sort()
        stop1 = timeit.default_timer()
        print('Time of optimized algorithm: ', stop1 - start1)
        time15 = stop - start
        time16 = stop1 - start1
        if time15 > time16:
            print("optimized algorithm has better performance")
            my_lable = Label(root, text="optimized algorithm has better performance and "
                                        f"my algorithm time is: {time15} and "
                                        f"the optimized algorithm is: {time16}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)
        else:
            print("my written algortihm has better performance")
            my_lable = Label(root, text="my algorithm has better performance and "
                                        f"my algorithm time is: {time15} and "
                                        f"the optimized algorithm is: {time16}", bg="black", fg="white")
            my_lable.grid(row=1, column=0)


frame = Frame(root, width=900, height=300, bg="black")
frame.grid(row=0, column=0, padx=10, pady=5)
l1 = Label(frame, text="Algorithm: ", bg="black", fg="white")
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)
a1 = Button(frame, text="Sort", command=sort, bg="#808080", fg="black")
a1.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
