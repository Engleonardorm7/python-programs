# def remove_duplicates(some_list):
#     without_duplicates=[]
#     for element in some_list:
#         if element not in without_duplicates:
#             without_duplicates.append(element)

#     return without_duplicates

# def run():
#     random_list=[1,1,2,2,4]
#     print(remove_duplicates(random_list))

if __name__=="__main__":
    #run()
    random_list=[1,1,2,2,4]
    without_duplicates=set(random_list)
    print("holi" , without_duplicates)