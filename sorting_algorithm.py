def bubble_sort(the_list):
    for k in xrange(1,len(the_list)):
        for i in xrange(len(the_list)-k):
            if the_list[i]>the_list[i+1]:
                the_list[i],the_list[i+1]=the_list[i+1],the_list[i]
        print the_list
    return the_list
#bubble_sort([19, 1, 9, 7, 3, 10, 13, 15, 8, 12])
