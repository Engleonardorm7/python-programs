import random

def bubble_sort(list):
    n=len(list)
    for i in range(n):   
        index=i
        actual_num=list[i]
        while index>0 and list[index-1]>actual_num:
            list[index]=list[index-1]
            index-=1

        list[index]=actual_num


    return list

if __name__=="__main__":

    list_size=int(input("What is the size of the list?"))

    list=[random.randint(0,100) for i in range(list_size)]
    print(list)

    ordered_list=bubble_sort(list)
    print(ordered_list)